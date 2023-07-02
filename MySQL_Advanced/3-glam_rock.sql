-- Lists all bands with Glam rock as
-- their main style, ranked by their longevity
SELECT
    BAND_NAME,
    (IFNULL(SPLIT,
    2020) - FORMED) AS LIFESPAN
FROM
    METAL_BANDS
WHERE
    STYLE REGEXP 'Glam rock'
ORDER BY
    LIFESPAN DESC;