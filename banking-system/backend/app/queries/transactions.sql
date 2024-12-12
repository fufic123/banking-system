-- SELECT ALL
SELECT * FROM transactions;

-- SELECT BY ID
SELECT * FROM transactions WHERE transaction_id = $1;

-- INSERT
INSERT INTO transactions (account_id, amount, transaction_type, performed_via, atm_id, branch_id, destination_account_id)
VALUES ($1, $2, $3, $4, $5, $6, $7)
RETURNING *;

-- UPDATE
UPDATE transactions
SET account_id = $2,
    amount = $3,
    transaction_type = $4,
    performed_via = $5,
    atm_id = $6,
    branch_id = $7,
    destination_account_id = $8,
    performed_at = NOW()
WHERE transaction_id = $1
RETURNING *;

-- DELETE
DELETE FROM transactions WHERE transaction_id = $1 RETURNING *;
