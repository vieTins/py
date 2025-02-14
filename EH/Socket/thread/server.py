# xử lý nhiều client cùng một lúc 
import socket 
import threading 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print('Server is listening...')

# Xử lý từng client trên luồn riêng 
def handle_client(client_socket , client_address) : 
    print(f"Connect from {client_address}")
    while True : 
        try:  
            data = client_socket.recv(1024).decode()            
            if not data : 
                break 
            else :
                print(f"Received: {data}")
                client_socket.sendall(data.encode())
        except:
            break
    print(f"Close connection from {client_address}")
    client_socket.close()

# Chấp nhận nhiều client và xử lý trên nhiều luồng
# Mỗi client sẽ được xử lý trên một luồng riêng 
while True: 
    clien_socket  , client_address = server_socket.accept()
    thread = threading.Thread(target=handle_client , args=(clien_socket , client_address))
    thread.start()