SELECT r.id, r.name
FROM rooms  AS r
JOIN students AS s ON s.room = r.id 
GROUP BY r.id, r.name
ORDER BY AVG(AGE(s.birthday))
LIMIT 5;

