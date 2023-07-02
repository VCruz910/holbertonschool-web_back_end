-- SQL script that creates a function SafeDiv
-- that divides (and returns) the first by
-- the second number or returns 0 if
-- the second number is equal to 0.

DELIMITER /
/

DROP FUNCTION IF EXISTS SAFEDIV;

CREATE FUNCTION SAFEDIV(
    A INT,
    B INT
) RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN (IF (B = 0, 0, A / B));
END // DELIMITER;