# Socket là điểm cuối trong giao tiếp mạng giữa hai thiết bị . 
# Một socket được tạo ra để giao tiếp giữa client và server.
import socket 
# Tạo socket tcp 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
# Lắng nghe tối đa 5 client 
server_socket.listen(5)
print('Server is listening...')

# Chấp nhận kết nối từ client
client_socket, client_address = server_socket.accept()
print(f'Connection from {client_address}')

# Nhận dữ liệu từ client
data = client_socket.recv(1024).decode() # 1024 là buffer size - chỉ nhận 1024 bytes = 1KB và decode() để chuyển dữ liệu từ byte sang string
print(f'Received: {data}')

# Gửi dữ liệu cho client
client_socket.sendall('Hello from server'.encode()) # encode() để chuyển dữ liệu từ string sang byte

# Đóng kết nối
client_socket.close()
server_socket.close()