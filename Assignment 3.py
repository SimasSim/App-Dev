# Program Name: Assignment 3.py
# Course: IT3883/Section W02
# Student Name: Simas Simokaitis
# Assignment Number: Assignment 3
# Due Date: 02/23/2025
# Purpose: A GUI application to convert Miles per Gallon into Kilometers per Liter
# List Specific resources used to complete the assignment
import tkinter as tk  # imports tkinter to make the gui with
from tkinter import StringVar  # allows dynamic changes to the gui

def convert_mpg_to_kmpl(*args): # creates the function
    try:
        mpg = float(mpg_var.get())  # gets inout value and sets to float
        kmpl = mpg * 0.425143707  # converts mpg to km/l
        result_var.set(f"{kmpl:.2f} km/L")  # updates the result
    except ValueError:  # handles errors
        result_var.set("Invalid input")

root = tk.Tk()  # Creates the main application window
root.title("MPG to KM/L Converter")  # sets the title
root.geometry("300x150")  # sets the size

mpg_var = StringVar()  # sets the input dynamically
mpg_var.trace_add("write", convert_mpg_to_kmpl)  # calls the function when the value updates
result_var = StringVar()  # stores the km/l value
result_var.set("0.00 km/L")  # sets the display

tk.Label(root, text="Miles per Gallon (MPG):").pack(pady=5)  # Makes a label for user input
mpg_entry = tk.Entry(root, textvariable=mpg_var)  # creates an input field for mpg
mpg_entry.pack(pady=5)  # puts the field below the label

tk.Label(root, text="Kilometers per Liter (KM/L):").pack(pady=5)  # makes a label for the output
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"))  # makes the display for the km/l
result_label.pack(pady=5)  # places field below the label

root.mainloop()  # Runs the application
