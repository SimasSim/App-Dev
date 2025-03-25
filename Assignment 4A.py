# Program Name: Assignment 4A.py
# Course: IT3883/Section W02
# Student Name: Simas Simokaitis
# Assignment Number: Assignment 4
# Due Date: 03/24/2025
# Purpose: two small python programs to implement basic network communications
# List Specific resources used to complete the assignment

# Program A (Client)
import socket


def client_program():
    host = '127.0.0.1'  # Localhost
    port = 40001  # Chosen port

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Enter message: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

    client_socket.close()


if __name__ == "__main__":
    client_program()
