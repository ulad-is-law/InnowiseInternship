CREATE TABLE IF NOT EXISTS rooms (
    id  INT PRIMARY KEY,
    name VARCHAR(15)
);

CREATE TABLE IF NOT EXISTS students (
    birthday TIMESTAMP,
    id  INT PRIMARY KEY,
    name VARCHAR(255),
    room SMALLINT,
    sex CHAR(1),

    FOREIGN KEY (room) REFERENCES rooms(id)
);