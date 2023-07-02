-- With these attributes:
-- id, integer, never null, auto increment and primary key
-- email, string (255 characters), never null and unique
-- name, string (255 characters)
-- country, enumeration of countries: US, CO and TN,
-- never null (= default will be the first element of the enumeration, here US)


CREATE TABLE IF NOT EXISTS USERS (
    ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    EMAIL VARCHAR(255) NOT NULL UNIQUE,
    NAME VARCHAR(255),
    COUNTRY ENUM ('US', 'CO', 'TN') NOT NULL
);