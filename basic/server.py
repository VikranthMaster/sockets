import socket

# HOST = socket.gethostbyname(socket.gethostbyname())
HOST = '192.168.1.39'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen() #number incdicates how many connections we are expecting

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    communication_socket.send(f"Got your msg!".encode('utf-8'))
    communication_socket.close()
    print(f"Connection with {address} ended!")
