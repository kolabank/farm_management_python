DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS farms;


CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE farms(
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER NOT NULL,
farmname TEXT NOT NULL,
location TEXT NOT NULL,
description TEXT,
longitude REAL,
latitude REAL,
FOREIGN KEY (user_id) REFERENCES users (id)
);