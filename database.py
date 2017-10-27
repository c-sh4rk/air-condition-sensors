import mysql.connector

connection = mysql.connector.connect(
    user="root",
    password="mysql37",
    host="localhost",
    database="sensors"
)

cursor = connection.cursor()
