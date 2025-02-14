import socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True :
    data = input("Enter message - Enter 'exit' to exit: ")
    client_socket.send(data.encode())
    if data == 'exit' : 
        break
    reponse = client_socket.recv(1024).decode()
    print(f"Received: {reponse}")

client_socket.close()