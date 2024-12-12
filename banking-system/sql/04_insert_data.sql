INSERT INTO customers (full_name, email, phone) VALUES
('John Doe', 'john@example.com', '123456789'),
('Jane Smith', 'jane@example.com', '987654321');

-- We'll select these to get their UUIDs if needed:
-- SELECT * FROM customers;

INSERT INTO accounts (customer_id, account_type, balance) 
SELECT customer_id, 'checking', 1000.00 
FROM customers WHERE email = 'john@example.com';

INSERT INTO accounts (customer_id, account_type, balance) 
SELECT customer_id, 'savings', 5000.00 
FROM customers WHERE email = 'john@example.com';

INSERT INTO accounts (customer_id, account_type, balance) 
SELECT customer_id, 'checking', 2000.00 
FROM customers WHERE email = 'jane@example.com';

INSERT INTO cards (customer_id, card_number, pin, expiration_date)
SELECT customer_id, '1234123412341234', 'hashed_pin_1', '2025-12-31'
FROM customers WHERE email = 'john@example.com';

INSERT INTO cards (customer_id, card_number, pin, expiration_date)
SELECT customer_id, '4321432143214321', 'hashed_pin_2', '2026-06-30'
FROM customers WHERE email = 'jane@example.com';

INSERT INTO atms (location) VALUES ('Downtown'), ('Airport'), ('Mall');

INSERT INTO branches (address, city, state) VALUES
('123 Main St', 'Metropolis', 'NY'),
('456 High St', 'Gotham', 'NJ');

INSERT INTO employees (branch_id, full_name, role)
SELECT branch_id, 'Alice Branch', 'Manager' FROM branches LIMIT 1;

INSERT INTO employees (branch_id, full_name, role)
SELECT branch_id, 'Bob Teller', 'Teller' FROM branches LIMIT 1 OFFSET 0;

INSERT INTO employees (branch_id, full_name, role)
SELECT branch_id, 'Charlie Admin', 'Admin' FROM branches LIMIT 1 OFFSET 1;

-- Insert some transactions:
-- We need account_id from a known account. Let's just pick first inserted accounts by referencing their customer_id from known emails.
-- For demonstration, we can do:
-- SELECT account_id FROM accounts JOIN customers USING(customer_id) WHERE email='john@example.com';

-- Suppose we got account_id_a and account_id_b from above queries:
-- Insert transactions (assuming we know account_ids):
-- We'll just assume we run these after retrieving account_ids in a real scenario.

-- We'll do this dynamically:
-- For John (john@example.com):
-- Let's pick his first account (checking):
-- SELECT account_id INTO TEMP TABLE tmp_acc FROM accounts JOIN customers USING(customer_id) WHERE email='john@example.com' AND account_type='checking' LIMIT 1;
-- We'll do a rough guess to simplify here: We trust these queries would be run after fetching the UUIDs.

-- For demonstration only (In real scenario, you'd fetch the UUIDs):
-- We'll just assume we know them after a SELECT. Replace uuid placeholders with real UUIDs from your DB if needed.

-- Just for demonstration, insert transactions referencing actual UUIDs after fetch:
-- e.g., INSERT INTO transactions (account_id, amount, transaction_type, performed_via, atm_id) VALUES ('<account_uuid>', 100.00, 'withdrawal', 'atm', '<atm_uuid>');
