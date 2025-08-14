#!/usr/bin/python3
"""
Creates the database alx_book_store in MySQL server.
If it already exists, it will not fail.
"""

import mysql.connector
import os

def create_database():
    try:
        # Get MySQL credentials from environment variables
        db_user = os.getenv("MYSQL_USER", "root")
        db_pass = os.getenv("MYSQL_PASSWORD", "")
        db_host = os.getenv("MYSQL_HOST", "localhost")

        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
