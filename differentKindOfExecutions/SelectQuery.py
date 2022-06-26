from mysql.connector import connect, Error

try:
    with connect(host="localhost", user='root', password='Gonlinepro892!', database="m", auth_plugin='mysql_native_password') as conn:
        print(conn)
        sql_statement = """
        SELECT family, count(*) as count FROM instruments GROUP BY family;
        """
        with conn.cursor() as cursor:
            cursor.execute(sql_statement)
            data = cursor.fetchall()
            for i in data:
                print(i)
            # print(f"data/n")
            conn.commit()

except Error as e:
    print(e)