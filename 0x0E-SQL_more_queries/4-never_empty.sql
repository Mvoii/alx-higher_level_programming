-- creates a table id_not_null
-- description id(INT) NOT NULL with default value 1
-- name VARCHAR(255)
-- if the table id_not_null already exists, it should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(255)
);
