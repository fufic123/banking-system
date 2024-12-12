-- SELECT ALL
SELECT * FROM atms;

-- SELECT BY ID
SELECT * FROM atms WHERE atm_id = $1;

-- INSERT
INSERT INTO atms (location, status) VALUES ($1, $2) RETURNING *;

-- UPDATE
UPDATE atms SET location = $2, status = $3 WHERE atm_id = $1 RETURNING *;

-- DELETE
DELETE FROM atms WHERE atm_id = $1 RETURNING *;
