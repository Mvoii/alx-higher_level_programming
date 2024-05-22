-- creates table unique_id
-- description: id(INT) default value 1, must be UNIQUE
-- name: VARCHAR(255)
-- if the table unique_id alredy exists, teh script should not fail

CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
