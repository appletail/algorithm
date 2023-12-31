-- 코드를 입력하세요
WITH RECURSIVE HOURS AS (
    SELECT 0 AS NUM
    UNION ALL
    SELECT NUM + 1
    FROM HOURS
    WHERE NUM < 23
)

SELECT H.NUM, IFNULL(AO.COUNT, 0) AS COUNT
FROM (SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT FROM ANIMAL_OUTS GROUP BY HOUR ) AS AO
    RIGHT JOIN HOURS AS H
    ON AO.HOUR = H.NUM