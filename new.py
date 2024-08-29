import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    username="root_yogesh",
    password="cG9aczQ$1",
    database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("update employee set ID=5 where ID=10")
mydb.commit()
print(mycursor.rowcount,"record affected")