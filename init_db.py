# startup.py
import os
from dotenv import load_dotenv
import MySQLdb

load_dotenv()

def init_database():
    try:
        connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd=os.getenv('MYSQL_ROOT_PASSWORD')
        )
        cursor = connection.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('MYSQL_DATABASE')}")
        cursor.execute(f"CREATE USER IF NOT EXISTS '{os.getenv('MYSQL_USER')}'@'localhost' IDENTIFIED BY '{os.getenv('MYSQL_PASSWORD')}'")
        cursor.execute(f"GRANT ALL PRIVILEGES ON {os.getenv('MYSQL_DATABASE')}.* TO '{os.getenv('MYSQL_USER')}'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")
        
        connection.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    init_database()