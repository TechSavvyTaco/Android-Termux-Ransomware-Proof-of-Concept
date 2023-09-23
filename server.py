import socket

# Configure the server
HOST = '127.0.0.1'  # Listen on all available interfaces
PORT = 8080       # Port to listen on

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

# Accept incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Handle client data here
    data = client_socket.recv(1024)
    print(f"KEY: {data.decode('utf-8')}")

    # Respond to the client
    response = "Please wait....."
    client_socket.send(response.encode('utf-8'))
    client_socket.close()