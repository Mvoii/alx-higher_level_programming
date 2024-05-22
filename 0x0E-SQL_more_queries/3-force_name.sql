-- creates the table force_name on the server
-- description is id(INT), name(VARCHAR(255)) NOT NULL
-- if the table force_name exists the script should not fail

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(255) NOT NULL
);
