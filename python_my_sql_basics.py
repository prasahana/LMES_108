import mysql.connector as sql_conn

"""pip install mysql-connector-python"""

try:
    connection = sql_conn.connect(host="127.0.0.1",
                                  username="admin",
                                  password="admin@123",
                                  database="uptor_108")

    my_cursor = connection.cursor()
    my_output = my_cursor.execute("show databases")
    print(my_output)
except Exception as ex:
    print(ex)

print(connection)
print("mysql executed successfully")