SELECT E.name
FROM Employee E
where E.id IN(
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId