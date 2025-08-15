SELECT r.id, r.name
FROM rooms  AS r
JOIN students AS s ON s.room = r.id 
GROUP BY r.id, r.name
HAVING COUNT(DISTINCT sex) = 1;
