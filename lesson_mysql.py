import mysql.connector

conn = mysql.connector.connect()

cursor = conn.cursor()

cursor.execute(

    'create database test_mysql_database'
)
cursor.close()
conn.close()