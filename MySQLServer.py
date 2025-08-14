#!/usr/bin/python3
"""
Creates the database alx_book_store in MySQL server.
If it already exists, it will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust username & password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # change if needed
            password="your_password"  # change if needed
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
