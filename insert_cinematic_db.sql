-- Fill directors table
INSERT INTO directors (name,surname,rating) VALUES ('Frank', 'Darabont', 7);
INSERT INTO directors (name,surname,rating) VALUES ('Francis Ford', 'Coppola', 8);
INSERT INTO directors (name,surname,rating) VALUES ('Quentin', 'Tarantino', 10);
INSERT INTO directors (name,surname,rating) VALUES ('Christopher', 'Nolan', 9);
INSERT INTO directors (name,surname,rating) VALUES ('David', 'Fincher', 7);

-- Fill movies table
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('The Shawshank Redemption', 1994, 'Drama', 1, 8);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('The Green Mile', 1999, 'Drama', 1, 6);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('The Godfather', 1972, 'Crime', 2, 7);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('The Godfather III', 1990, 'Crime', 2, 6);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('Pulp Fiction', 1994, 'Crime', 3, 9);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('Inglourious Basterds', 2009, 'War', 3, 8);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('The Dark Knight', 2008, 'Action', 4, 9);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('Interstellar', 2014, 'Sci-fi', 4, 8);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('The Prestige', 2006, 'Drama', 4, 10);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('Fight Club', 1999, 'Drama', 5, 7); 
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('Zodiac', 2007, 'Crime', 5, 5);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('Seven', 1995, 'Drama', 5, 8);
INSERT INTO movies (title,year,category,director_id,rating) VALUES ('Alien 3', 1992, 'Horror', 5, 5);
