import sqlite3
import math

# Create a database connection
def create_connection():
    conn = sqlite3.connect('calculator_history.db')
    return conn

# Create the table for storing history if it doesn't exist
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        operation TEXT,
                        result REAL
                    )''')
    conn.commit()
    conn.close()

# Insert operation into the database
def insert_history(operation, result):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (operation, result) VALUES (?, ?)", (operation, result))
    conn.commit()
    conn.close()

# Retrieve history from the database
def view_history():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Basic arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Scientific functions
def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Negative number cannot have a real square root."

def logarithm(x, base=10):
    if x > 0:
        return math.log(x, base)
    else:
        return "Error! Logarithm of non-positive number is undefined."

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Main calculator function
def calculator():
    print("Welcome to the Python Scientific Calculator!")
    print("Operations: +, -, *, /, sqrt, log, sin, cos, tan")
    print("Type 'history' to view past calculations or 'exit' to quit.")

    while True:
        operation = input("Enter operation: ").strip().lower()

        if operation == 'exit':
            print("Goodbye!")
            break
        elif operation == 'history':
            history = view_history()
            if history:
                print("History of calculations:")
                for record in history:
                    print(f"{record[1]} = {record[2]}")
            else:
                print("No history found.")
        else:
            try:
                if operation in ['+', '-', '*', '/']:
                    x = float(input("Enter first number: "))
                    y = float(input("Enter second number: "))
                    if operation == '+':
                        result = add(x, y)
                    elif operation == '-':
                        result = subtract(x, y)
                    elif operation == '*':
                        result = multiply(x, y)
                    elif operation == '/':
                        result = divide(x, y)
                elif operation == 'sqrt':
                    x = float(input("Enter number: "))
                    result = square_root(x)
                elif operation == 'log':
                    x = float(input("Enter number: "))
                    base = float(input("Enter base (default is 10): ") or 10)
                    result = logarithm(x, base)
                elif operation == 'sin':
                    x = float(input("Enter angle in degrees: "))
                    result = sine(x)
                elif operation == 'cos':
                    x = float(input("Enter angle in degrees: "))
                    result = cosine(x)
                elif operation == 'tan':
                    x = float(input("Enter angle in degrees: "))
                    result = tangent(x)
                else:
                    print("Invalid operation.")
                    continue

                print(f"Result: {result}")
                insert_history(f"{operation}({x}, {y if operation in ['+', '-', '*', '/'] else ''})", result)
            except ValueError:
                print("Invalid input! Please enter numbers.")
            except Exception as e:
                print(f"Error: {e}")

# Main execution
if __name__ == '__main__':
    create_table()  # Create table if not exists
    calculator()  # Run the calculator app
