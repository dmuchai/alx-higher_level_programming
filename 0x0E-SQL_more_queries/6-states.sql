-- creates a database hbtn_0d_usa and a table states (in the database)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;
-- create table states in the database hbtn_0d_usa
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
