import os
import time
from dotenv import load_dotenv
import MySQLdb

load_dotenv()

def init_database():
    retries = 30
    while retries > 0:
        try:
            connection = MySQLdb.connect(
                host="db",
                user="root",
                passwd=os.getenv('MYSQL_ROOT_PASSWORD')
            )
            cursor = connection.cursor()
            
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('MYSQL_DATABASE')}")
            cursor.execute(f"CREATE USER IF NOT EXISTS '{os.getenv('MYSQL_USER')}'@'%' IDENTIFIED BY '{os.getenv('MYSQL_PASSWORD')}'")
            cursor.execute(f"GRANT ALL PRIVILEGES ON {os.getenv('MYSQL_DATABASE')}.* TO '{os.getenv('MYSQL_USER')}'@'%'")
            cursor.execute("FLUSH PRIVILEGES")
            
            connection.close()
            return
            
        except Exception as e:
            print(f"Error: {e}")
            retries -= 1
            if retries > 0:
                print(f"Retrying in 2 seconds... ({retries} attempts left)")
                time.sleep(2)
            else:
                print("Max retries reached. Database initialization failed.")
                raise

if __name__ == "__main__":
    init_database()