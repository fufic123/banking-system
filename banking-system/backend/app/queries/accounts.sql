-- SELECT ALL
SELECT * FROM accounts;

-- SELECT BY ID
SELECT * FROM accounts WHERE account_id = $1;

-- INSERT
INSERT INTO accounts (customer_id, account_type, balance) VALUES ($1, $2, $3) RETURNING *;

-- UPDATE
UPDATE accounts SET account_type = $2, balance = $3 WHERE account_id = $1 RETURNING *;

-- DELETE
DELETE FROM accounts WHERE account_id = $1 RETURNING *;
