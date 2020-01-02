import mysql.connector

def connect_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database="nova_prime"
    )
    return mydb