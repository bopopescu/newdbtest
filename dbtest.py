import mysql.connector
import sys

conn = mysql.connector.connect(host='localhost',
                               user='carleton',
                               password='??????',
                               db='world_x')
# cursorclass=pymysql.cursors.DictCursor)
# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = conn.cursor()

# Use all the SQL you like
cur.execute("select * from city")

# print all records = cursor.fetchall()
# the first cell of all the rows
records = cur.fetchall()

for row in records:
    print(row)


# close connection
print("Connection closing")
cur.close()
conn.close()
exit()
