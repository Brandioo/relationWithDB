from mysql.connector import connect, Error

try:
    with connect(host="localhost", user='root', password='Gonlinepro892!', database="cinematic") as conn:
        print(conn)
        sql_statement = """
        select 1000
        """
        with conn.cursor() as cursor:
            cursor.execute(sql_statement)
            data = cursor.fetchall()
            print(data)
            #conn.commit()

except Error as e:
    print(e)