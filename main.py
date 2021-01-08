import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Uzair2005"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
