-- creates database hbtn_0d_usa and a table in it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id)
);
