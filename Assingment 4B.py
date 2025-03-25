# Program Name: Assignment 4B.py
# Course: IT3883/Section W02
# Student Name: Simas Simokaitis
# Assignment Number: Assignment 4
# Due Date: 03/24/2025
# Purpose: two small python programs to implement basic network communications
# List Specific resources used to complete the assignment

# Program B (Server)
import socket


def server_program():
    host = '127.0.0.1'
    port = 40001

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")

    data = conn.recv(1024).decode()
    print(f"Received: {data}")

    response = data.upper()
    conn.send(response.encode())

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    server_program()
