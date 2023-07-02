-- Add bonus

DELIMITER $$

CREATE PROCEDURE ADDBONUS(
    IN USER_ID INTEGER,
    IN PROJECT_NAME VARCHAR(255),
    IN SCORE INTEGER
)
BEGIN
    INSERT INTO PROJECTS(
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
                    NAME = PROJECT_NAME LIMIT 1
            );
    INSERT INTO CORRECTIONS (
        USER_ID,
        PROJECT_ID,
        SCORE
    ) VALUES(
        USER_ID,
        (SELECT ID FROM PROJECTS WHERE NAME = PROJECT_NAME),
        SCORE
    );
END $$ DELIMITER;