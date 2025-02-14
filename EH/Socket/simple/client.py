import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_socket.sendall('Hello from client'.encode())

# Nhận phản hồi từ server
reponse = client_socket.recv(1024).decode() 
print(f'Received: {reponse}')

client_socket.close()