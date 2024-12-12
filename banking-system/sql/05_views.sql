DROP VIEW IF EXISTS v_customer_transactions CASCADE;

CREATE VIEW v_customer_transactions AS
SELECT c.full_name AS customer_name,
       a.account_type,
       t.amount,
       t.transaction_type,
       t.performed_at
FROM customers c
JOIN accounts a ON a.customer_id = c.customer_id
JOIN transactions t ON t.account_id = a.account_id;
