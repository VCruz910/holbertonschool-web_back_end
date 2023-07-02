-- Creates an index idx_name_first_score on
-- the table names and the first letter of name and the score.
CREATE INDEX IDX_NAME_FIRST_SCORE ON NAMES(
    NAME(1),
    SCORE
);