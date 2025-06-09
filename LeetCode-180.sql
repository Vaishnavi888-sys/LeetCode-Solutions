SELECT DISTINCT num AS ConsecutiveNums
FROM(
    SELECT num,
    LEAD(num,1) OVER (ORDER BY id) AS N1,
    LEAD(num,2) OVER (ORDER BY id) AS N2
    FROM Logs
) AS temp
WHERE num = N1 AND num = N2;
