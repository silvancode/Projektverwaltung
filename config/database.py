import mysql.connector
from mysql.connector import Error
from config.settings import DATABASE_CONFIG


def create_connection():
    try:
        connection = mysql.connector.connect(
            host=DATABASE_CONFIG['host'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            database=DATABASE_CONFIG['database'],
            port=3306
        )
        if connection.is_connected():
            print("Verbindung zu MySQL hergestellt.")
        return connection
    except Error as e:
        print(f"Fehler bei der Verbindung zu MySQL: {e}")
        return None
