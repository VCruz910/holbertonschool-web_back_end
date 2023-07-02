-- SQL script that creates a view need_meeting
-- that lists all students that have a score
-- under 80 (strict) and no last_meeting or
-- more than 1 month.

DROP VIEW IF EXISTS NEED_MEETING;

CREATE VIEW NEED_MEETING AS
    SELECT
        NAME
    FROM
        STUDENTS
    WHERE
        SCORE < 80
        AND (STUDENTS.LAST_MEETING IS NULL
        OR STUDENTS.LAST_MEETING < DATE_ADD(NOW(),
        INTERVAL -1 MONTH));

FOOTER