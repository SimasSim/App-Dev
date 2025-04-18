# Program Name: Assignment 5.py
# Course: IT3883/Section W02
# Student Name: Simas Simokaitis
# Assignment Number: Assignment 5
# Due Date: 04/18/2025
# Purpose: Write a Python program to create and interact with a database.
# List Specific resources used to complete the assignment

import sqlite3

def main():
    # Step 1: Connect to (or create) the database
    conn = sqlite3.connect('temperature_data.db')
    cursor = conn.cursor()

    # Step 2: Create the table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS TemperatureReadings (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Day_Of_Week TEXT,
            Temperature_Value REAL
        )
    ''')

    # Step 3: Read the file and insert data
    with open('Assignment5input.txt', 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                day, temp = parts
                try:
                    cursor.execute('''
                        INSERT INTO TemperatureReadings (Day_Of_Week, Temperature_Value)
                        VALUES (?, ?)
                    ''', (day.strip(), float(temp.strip())))
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")

    conn.commit()

    # Step 4: Query for averages (case-insensitive)
    for day in ['Sunday', 'Thursday']:
        cursor.execute('''
            SELECT AVG(Temperature_Value)
            FROM TemperatureReadings
            WHERE LOWER(Day_Of_Week) = LOWER(?)
        ''', (day,))
        result = cursor.fetchone()[0]
        if result is not None:
            print(f"Average temperature for {day}: {result:.2f}")
        else:
            print(f"No data found for {day}")

    # Step 5: Close the connection
    conn.close()

if __name__ == '__main__':
    main()