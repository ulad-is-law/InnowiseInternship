CREATE TABLE students IF NOT EXISTS(
    birthday TIMESTAMP,
    id  INT PRIMARY KEY,
    name VARCHAR(255),
    room SMALLINT,
    sex CHAR(1),

    FOREIGN KEY (room) REFERENCES rooms(id)
)

CREATE TABLE rooms IF NOT EXISTS(
    id  INT PRIMARY KEY,
    name VARCHAR(15)
)