SELECT r.id, r.name
FROM rooms  AS r
JOIN students AS s ON s.room = r.id 
GROUP BY r.id
ORDER BY  MAX(AGE(s.birthday)) - MIN(AGE(s.birthday)) DESC
LIMIT 5;

