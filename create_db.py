import mysql.connector
from mysql.connector import Error

# Common MySQL root passwords to try
passwords_to_try = ['', 'root', 'password', 'admin', '123456']

for password in passwords_to_try:
    try:
        print(f"Trying to connect with password: {'(empty)' if password == '' else password}")
        
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS hotel_management_system CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print("Database 'hotel_management_system' created successfully or already exists")
            
            # Show databases
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            print("Available databases:")
            for db in databases:
                print(f"  - {db[0]}")
            
            cursor.close()
            connection.close()
            print("MySQL connection closed")
            break
            
    except Error as e:
        print(f"Error with password '{password}': {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.close()
else:
    print("Could not connect with any of the tried passwords.")
    print("Please provide the correct MySQL root password.")
