import mysql.connector

def fetch_users_starting_with_a():
    try:
        # Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="users"
        )
        cursor = conn.cursor()

        # Execute the query
        query = "SELECT * FROM users WHERE name LIKE 'A%';"
        cursor.execute(query)

        # Fetch all matching rows
        results = cursor.fetchall()

        # Print the results
        print("Users starting with the letter 'A':")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    fetch_users_starting_with_a()
"""
During the interview, I focused first on creating the database first.
After reviewing my previous work with SQL during Foundations, I saw
how I prepared the python scripts correctly, which was what was asked for.
"""