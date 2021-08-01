import mysql.connector

# establish connection to MySQL database using mysql.connector.connect method  

dbconnection = mysql.connector.connect(host ='localhost',user='om',passwd='Test@123',database='pydbtest')

# create a mysql cursor with cursor method

dbcursor = dbconnection.cursor()

# print(dbconnection)

# print(dbcursor)

# print(dbcursor.execute("show tables"))