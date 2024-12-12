-- SELECT ALL
SELECT * FROM employees;

-- SELECT BY ID
SELECT * FROM employees WHERE employee_id = $1;

-- INSERT
INSERT INTO employees (branch_id, full_name, role) VALUES ($1, $2, $3) RETURNING *;

-- UPDATE
UPDATE employees SET branch_id = $2, full_name = $3, role = $4 WHERE employee_id = $1 RETURNING *;

-- DELETE
DELETE FROM employees WHERE employee_id = $1 RETURNING *;
