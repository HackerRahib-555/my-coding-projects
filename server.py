import socket
import threading

server_ip = '127.0.0.1'
server_port = 6549

# Create and bind server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(10)
print("Server is waiting for users...")

clients = {}  # client_socket -> username
lock = threading.Lock()

# Function to handle each client
def handle_client(client_socket):
    # Ask for a username upon connection
    client_socket.send("Enter your username: ".encode())
    while True:
        username = client_socket.recv(1024).decode('utf-8').strip()

        with lock:
            if username in clients.values():
                client_socket.send(b"Username already taken. Please try again: ")
            else:
                clients[client_socket] = username
                break

    print(f"{username} connected")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"{username} has disconnected")
                break

            # Print message with username
            print(f"{username}: {message}")

            # Broadcast the message to all clients
            with lock:
                for client in clients:
                      
                    client.send(f"{username}: {message}".encode())

        except Exception as e:
            print(f"Error with {username}: {e}")
            break

    # Remove client and close connection
    with lock:
        del clients[client_socket]
    print(f"{username} disconnected")
    client_socket.close()

# Function to accept incoming connections
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        
        client_thread.start()

# Start accepting connections
accept_connections()