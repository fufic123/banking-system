-- Create accounts/card trigger (unchanged from previous)
CREATE OR REPLACE FUNCTION create_customer_accounts_and_card()
RETURNS TRIGGER AS $$
DECLARE
    cust_id UUID := NEW.customer_id;
    card_num VARCHAR(16);
    hashed_pin VARCHAR(60);
BEGIN
    card_num := lpad((floor(random()*1e16)::bigint)::text,16,'0');
    hashed_pin := 'hashed_pin_1';  -- placeholder
    
    INSERT INTO accounts (customer_id, account_type, balance)
    VALUES (cust_id, 'checking', 0.00);
    
    INSERT INTO accounts (customer_id, account_type, balance)
    VALUES (cust_id, 'savings', 0.00);

    INSERT INTO cards (customer_id, card_number, pin, expiration_date, active)
    VALUES (cust_id, card_num, hashed_pin, CURRENT_DATE + INTERVAL '3 years', TRUE);

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_create_accounts_card
AFTER INSERT ON customers
FOR EACH ROW
EXECUTE PROCEDURE create_customer_accounts_and_card();


-- Update account balance trigger with deposit, withdrawal, and transfer logic
CREATE OR REPLACE FUNCTION update_account_balance()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.transaction_type = 'deposit' THEN
        UPDATE accounts SET balance = balance + NEW.amount WHERE account_id = NEW.account_id;

    ELSIF NEW.transaction_type = 'withdrawal' THEN
        UPDATE accounts SET balance = balance - NEW.amount WHERE account_id = NEW.account_id;

    ELSIF NEW.transaction_type = 'transfer' THEN
        -- For a transfer, account_id is the source account
        -- destination_account_id is the target account
        -- First, deduct from source
        UPDATE accounts SET balance = balance - NEW.amount WHERE account_id = NEW.account_id;
        -- Then, add to destination
        UPDATE accounts SET balance = balance + NEW.amount WHERE account_id = NEW.destination_account_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_balance
AFTER INSERT ON transactions
FOR EACH ROW
EXECUTE PROCEDURE update_account_balance();


-- Prevent negative balance trigger:
-- For withdrawal and transfer (source side), ensure no negative.
CREATE OR REPLACE FUNCTION prevent_negative_balance()
RETURNS TRIGGER AS $$
DECLARE
    acc_balance NUMERIC(12,2);
BEGIN
    SELECT balance INTO acc_balance FROM accounts WHERE account_id = NEW.account_id;

    IF NEW.transaction_type = 'withdrawal' OR NEW.transaction_type = 'transfer' THEN
        IF acc_balance - NEW.amount < 0 THEN
            RAISE EXCEPTION 'Insufficient funds';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_prevent_negative_balance
BEFORE INSERT ON transactions
FOR EACH ROW
EXECUTE PROCEDURE prevent_negative_balance();


-- Daily summary triggers unchanged
CREATE TABLE IF NOT EXISTS daily_transaction_summary (
    summary_date DATE PRIMARY KEY,
    total_amount NUMERIC(12,2) DEFAULT 0.00,
    transaction_count INT DEFAULT 0
);

CREATE OR REPLACE FUNCTION summarize_daily_transactions()
RETURNS TRIGGER AS $$
DECLARE
    today DATE := CURRENT_DATE;
    total NUMERIC(12,2);
    countx INT;
BEGIN
    SELECT SUM(amount), COUNT(*) INTO total, countx FROM transactions WHERE performed_at::DATE = today;
    UPDATE daily_transaction_summary
    SET total_amount = COALESCE(total,0), transaction_count = COALESCE(countx,0)
    WHERE summary_date = today;

    IF NOT FOUND THEN
        INSERT INTO daily_transaction_summary (summary_date, total_amount, transaction_count)
        VALUES (today, COALESCE(total,0), COALESCE(countx,0));
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_daily_summary
AFTER INSERT ON transactions
FOR EACH STATEMENT
EXECUTE PROCEDURE summarize_daily_transactions();
