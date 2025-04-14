from config import DB_HOST, DB_USER, DB_NAME, DB_PASSWORD
import mysql.connector

#A CONEXÃO DO DB

def create_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )