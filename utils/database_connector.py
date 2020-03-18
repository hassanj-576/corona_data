import mysql.connector

from Config import DB_DB, DB_HOST, DB_PASSWORD, DB_USER


def create_connection():
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASSWORD,
        database=DB_DB
    )

    mycursor = mydb.cursor()

    return mydb, mycursor
