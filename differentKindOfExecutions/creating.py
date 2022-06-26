from mysql.connector import connect, Error

try:
    db = connect(host="localhost", user='root', password='SDA19912022!', database="cinematic")
    print(db)
    print(type(db))
    with connect(host="localhost", user='root', password='SDA19912022!', database="cinematic") as conn:
        print(conn)
        print(type(conn))
        sql_statement = """
        CREATE TABLE IF NOT EXISTS directors(
        director_id int NOT NULL AUTO_INCREMENT,
        name varchar(255),
        surname varchar(255),
        rating int,
        PRIMARY KEY (director_id)
        );

        CREATE TABLE IF NOT EXISTS movies(
       movie_id int NOT NULL AUTO_INCREMENT,
        title varchar(255),
        year int,
        category varchar(255),
        director_id int,
        rating int,
       PRIMARY KEY (movie_id),
        FOREIGN KEY (director_id) REFERENCES directors(director_id)
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        # data = cursor.fetchall()
        # print(data)
        # conn.commit()
    cursor.close()
    db.close()
    conn.close()

except Error as e:
    print(e)