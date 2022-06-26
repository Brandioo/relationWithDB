from mysql.connector import connect, Error

try:
    with connect(host="localhost",user="root",passwd="ketaketa7.",database= 'models') as conn:
        sql_statement = """
        SELECT * from customers;
        """
        with conn.cursor() as cursor:
            cursor.execute(sql_statement)
            for i in cursor:
                print(i)



except Error as e:
    print(e)

#################################

db=connect(host="localhost", user="root", passwd="ketaketa7.",database= 'models')
sql_statement = """
        SELECT * from customers;
        """
mycursor=db.cursor()
mycursor.execute(sql_statement)

for i in mycursor:
    print(i)