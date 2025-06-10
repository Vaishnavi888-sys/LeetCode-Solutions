SELECT P.email
FROM Person P
GROUP BY email
HAVING COUNT(*) > 1;