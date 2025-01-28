# Program Name: Assignment 1.py
# Course: IT3883/Section W02
# Student Name: Simas Simokaitis
# Assignment Number: Assignment 1
# Due Date: 01/27/2025
# Purpose: Append data, clear input, display the input
# List Specific resources used to complete the assignment
Choice = 0  # sets up the choice variable that runs the while loop
words = str()  # sets up the words variable that is used to store the string
while Choice <= 3:  # the while loop that makes the program persist until the number 4 is answered
    Choice1 = input(  # ask the user for input based on the options
            "Option 1: Append data to the input buffer \n" #> options
            "   •This option will prompt the user for a string and append it to any previous input that has been provided. \n \n"
            "Option 2: Clear the input buffer \n"
            "   •This option will clear any data that has been previously input. \n \n"
            "Option 3: Display the input buffer \n"
            "   •This option will print to the screen whatever input data is currently being saved. \n \n"
            "Option 4: Exit the program \n \n")  #< options
    Choice = int(Choice1)  # sets choice var to int
    if Choice == 1:  # if statement for when selecting 1
        print("Enter String:")
        words = input()
        words = str(words)
        "\n"
    elif Choice == 2:
        print("String Cleared")
        words = ""
        "\n"
    elif Choice == 3:
        print(words)
        "\n"





