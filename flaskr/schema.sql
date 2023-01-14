DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS farms;
DROP TABLE IF EXISTS crops;
DROP TABLE IF EXISTS plantdetails;


CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
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

CREATE TABLE crops (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  cropname TEXT NOT NULL,
  cropbreed TEXT,
  FOREIGN KEY (user_id) REFERENCES users (id)
);


CREATE TABLE plantdetails(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  crop TEXT,
  crop_id INTEGER,
  date_planted TEXT,
  date_harvest TEXT,
  stands INTEGER,
  area REAL,
  FOREIGN KEY (crop_id) REFERENCES crops(id)
)