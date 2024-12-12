-- SELECT ALL
SELECT * FROM customers;

-- SELECT BY ID
SELECT * FROM customers WHERE customer_id = $1;

-- INSERT
INSERT INTO customers (full_name, email, phone) VALUES ($1, $2, $3) RETURNING *;

-- UPDATE
UPDATE customers SET full_name = $2, email = $3, phone = $4 WHERE customer_id = $1 RETURNING *;

-- DELETE
DELETE FROM customers WHERE customer_id = $1 RETURNING *;
