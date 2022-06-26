from mysql.connector import connect, Error

try:
    with connect(host="localhost", user='root', password='SDA19912022!', database="cinematic") as conn:
        print(conn)
        movies = """
        INSERT INTO movies
        (title,year,category,director_id,rating)
        VALUES ( %s, %s, %s, %s, %s )
        """
        movie_values = [
            ('Kill Bill: Vol. 1', 2003, 'Action', 3, 10),
            ('The Prestige', 2006, 'Mystery', 4, 10),
            ('Bram Stokers Dracula', 1992, 'Horror', 2, 8)
        ]
        with conn.cursor() as cursor:
            cursor.executemany(movies, movie_values)
            conn.commit()

except Error as e:
    print(e)