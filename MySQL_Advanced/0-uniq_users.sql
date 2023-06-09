-- Creates a table called users
-- with these attributes
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
--  If the table already exists, your script should not fail
--  Your script can be executed on any database

CREATE TABLE IF NOT EXISTS USERS (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    EMAIL VARCHAR(255) NOT NULL UNIQUE,
    NAME VARCHAR(255)
);