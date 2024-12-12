-- Row-level trigger to update account balance upon transaction
CREATE OR REPLACE FUNCTION update_account_balance()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.transaction_type = 'deposit' THEN
        UPDATE accounts SET balance = balance + NEW.amount WHERE account_id = NEW.account_id;
    ELSIF NEW.transaction_type = 'withdrawal' THEN
        UPDATE accounts SET balance = balance - NEW.amount WHERE account_id = NEW.account_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_balance
AFTER INSERT ON transactions
FOR EACH ROW
EXECUTE PROCEDURE update_account_balance();

-- Statement-level trigger for daily summary:
CREATE TABLE daily_transaction_summary (
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
