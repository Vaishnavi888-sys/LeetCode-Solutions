SELECT C.name 
FROM Customer C
WHERE C.referee_id NOT IN (2) OR C.referee_id IS NULL;