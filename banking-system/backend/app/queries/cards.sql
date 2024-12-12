-- SELECT ALL
SELECT * FROM cards;

-- SELECT BY ID
SELECT * FROM cards WHERE card_id = $1;

-- INSERT
INSERT INTO cards (customer_id, card_number, pin, expiration_date, active)
VALUES ($1, $2, $3, $4, $5) RETURNING *;

-- UPDATE
UPDATE cards SET card_number = $2, pin = $3, expiration_date = $4, active = $5 WHERE card_id = $1 RETURNING *;

-- DELETE
DELETE FROM cards WHERE card_id = $1 RETURNING *;
