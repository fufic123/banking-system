-- SELECT ALL
SELECT * FROM branches;

-- SELECT BY ID
SELECT * FROM branches WHERE branch_id = $1;

-- INSERT
INSERT INTO branches (address, city, state) VALUES ($1, $2, $3) RETURNING *;

-- UPDATE
UPDATE branches SET address = $2, city = $3, state = $4 WHERE branch_id = $1 RETURNING *;

-- DELETE
DELETE FROM branches WHERE branch_id = $1 RETURNING *;
