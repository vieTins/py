# Unpacking là một cách để giải nén các giá trị từ một chuỗi hoặc danh sách thành các biến rời rạc 
# Chú ý số lượng phần tử ở bên trái phải bằng số lượng phần tử ở bên phải

a = [1, 2, 3]
x, y, z = a
print(x, y, z)

# Nếu không muốn lấy hết các phần tử còn lại thì dùng dấu *
a = [1, 2, 3, 4, 5]
x, y, *z = a
print(x, y, z)

# nếu không muốn lấy phần tử nào thì dùng _
a = [1, 2, 3, 4, 5]
_, _, *z = a
print(z)

