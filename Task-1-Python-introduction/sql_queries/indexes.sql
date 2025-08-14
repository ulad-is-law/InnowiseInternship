CREATE INDEX IF NOT EXISTS students_room_idx ON students (room);
CREATE INDEX IF NOT EXISTS students_room_idx_hash ON students USING hash (room);
CREATE INDEX IF NOT EXISTS students_room_sex_idx ON students (room, sex);