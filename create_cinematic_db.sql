DROP DATABASE cinematic;
CREATE DATABASE cinematic;
USE cinematic;
CREATE TABLE directors(
    director_id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    surname varchar(255),
    rating int,
    PRIMARY KEY (director_id)
);
CREATE TABLE movies(
	movie_id int NOT NULL AUTO_INCREMENT,
    title varchar(255),
    year int,
    category varchar(255),
    director_id int,
    rating int,
	PRIMARY KEY (movie_id),
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);