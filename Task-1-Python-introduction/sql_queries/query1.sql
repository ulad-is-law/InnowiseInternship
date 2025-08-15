SELECT rooms.name, COUNT(students.id) AS amount_of_students
FROM rooms
LEFT JOIN students ON students.room = rooms.id
GROUP BY rooms.name;