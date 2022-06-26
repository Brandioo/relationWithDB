from mysql.connector import connect, Error

try:
    with connect(host="localhost",user="root",passwd="ketaketa7.",database= 'models') as conn:
        departments = """
        INSERT INTO payments
        (customerNumber, checkNumber,paymentDate,amount)
        VALUES ( %s, %s,%s,%s )
        """
        depts = [
            ("496", "ND7485700", "2004-08-21", "33347.90"),
            ("496", "ND7485777", "2004-08-22", "33350.91"),
            ("496", "ND7485778", "2004-08-23" ,   "33347.92")
        ]
        with conn.cursor() as cursor:
            cursor.executemany(departments, depts)
            conn.commit()


except Error as e:
    print(e)