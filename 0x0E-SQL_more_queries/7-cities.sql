-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server

-- create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use DB
USE hbtn_0d_usa;

-- create the table
CREATE TABLE IF NOT EXISTS hbtn_0d_usai.cities (
	id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256)
	);
