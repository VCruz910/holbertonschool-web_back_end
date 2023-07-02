-- Add bonus
DELIMITER $$

CREATE PROCEDURE ADDBONUS(
    IN USER_ID INT,
    PROJECT_NAME VARCHAR(255),
    SCORE FLOAT
)
BEGIN
    INSERT INTO PROJECTS (
        NAME
    )
        SELECT
            PROJECT_NAME
        FROM
            DUAL
        WHERE
            NOT EXISTS (
                SELECT
                    *
                FROM
                    PROJECTS
                WHERE
                    NAME = PROJECT_NAME
            );
    INSERT INTO CORRECTIONS (
        USER_ID,
        PROJECT_ID,
        SCORE
    ) VALUES (
        USER_ID,
        (SELECT ID FROM PROJECTS WHERE NAME = PROJECT_NAME),
        SCORE
    );
    END$$ DELIMITER;