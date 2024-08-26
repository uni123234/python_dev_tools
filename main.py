# error_handling.py

"""
This script demonstrates error handling for division operations and basic SQLite database interactions.

Functions:
- division_operation: Handles user input for division and manages errors.
- database_operation: Connects to an SQLite database, performs a query, and handles errors.

Instructions:
- Use this script to handle exceptions and manage database operations with proper error handling.
"""

"""
To create and manage a virtual environment for your project, follow these steps:

1. Create a virtual environment:
   $ python -m venv myenv

2. Activate the virtual environment:
   - On Windows:
     $ myenv\Scripts\activate.bat
   - On macOS/Linux:
     $ source myenv/bin/activate

3. Install a package using pip:
   (myenv) $ pip install package_name

4. List installed packages:
   (myenv) $ pip list

5. Deactivate the virtual environment:
   (myenv) $ deactivate
"""

import sqlite3


def division_operation():
    """
    Prompts the user to enter two numbers and performs division.
    Handles ValueError for invalid input and ZeroDivisionError for division by zero.
    """
    try:
        num1 = int(input("Введіть перше число: "))
        num2 = int(input("Введіть друге число: "))
        result = num1 / num2
        print(f"Результат: {result}")
    except ValueError:
        print("Помилка: Введені дані не є числами")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль неможливе")
    except (KeyboardInterrupt, EOFError):
        print("Операція була перервана")


def database_operation():
    """
    Connects to a SQLite database, executes a query to fetch all users, and prints the results.
    Handles SQLite database errors and ensures that the connection is closed properly.
    """
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.DatabaseError:
        print("Помилка: Помилка бази даних")
    except (KeyboardInterrupt, EOFError):
        print("Операція була перервана")
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    # Uncomment the function you want to run
    # division_operation()
    # database_operation()
    pass
