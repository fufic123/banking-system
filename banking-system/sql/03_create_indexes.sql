-- Create indexes to improve query performance

CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_accounts_customer_id ON accounts(customer_id);
CREATE INDEX idx_transactions_account_id ON transactions(account_id);
CREATE INDEX idx_transactions_performed_at ON transactions(performed_at);
CREATE INDEX idx_cards_card_number ON cards(card_number);
