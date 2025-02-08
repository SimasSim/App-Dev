# Program Name: Assignment 2.py
# Course: IT3883/Section W02
# Student Name: Simas Simokaitis
# Assignment Number: Assignment 2
# Due Date: 02/7/2025
# Purpose: calculate final averages of a group of students in descending grade order
# List Specific resources used to complete the assignment
students = []  # List to store (name, average) tuples
with open('Asgn2input.txt', 'r') as file: # Read the file and process student grades
    for line in file:
        data = line.strip().split()  # Split by spaces
        student = data[0]  # First element is the student's name
        grades = list(map(int, data[1:]))  # Convert grades to integers

        average = sum(grades) / len(grades)  # Find the average
        students.append((student, average))  # Store student name and average in the list
students.sort(key=lambda x: x[1], reverse=True)  # Sort students by average in descending order
for student, avg in students:
    print(f"{student} {avg:.2f}")  # Print student name and average with 2 decimal places
