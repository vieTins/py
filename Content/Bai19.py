# Set là một tập hợp các phần tử duy nhất không có thứ tự . Chúng thường được sử dụng để tính toán các phép toán liên quan tới tập hợp 
# Các phần tử trong set không có thứ tự nhất định nào cả  
# Các phần tử trong set là độc nhất , không có 2 phần tử nào trong set trùng nhau 
# Set không thể truy cập được thông qua chỉ số 
# Set có thể thay đổi 
# Toán tử in có độ pt ở set là O(1)
# Tạo set thì dùng dấu {}
s = {1,2,3,4,5,6,7,8,9,10}
print(s)

# set không thể lưu được những phần tử có thể thay đổi được giá trị như list 

a = [1,2,3,4,5,6,7,8,9,10]
b = set(a)

# Thêm phần tử vào set
b.add(11) # Nếu như có rồi thì không thêm 
# Thêm nhiều phần tử vào set có thể dùng hàm update
b.update({12,13,14,15})
print(b)

# Xóa phần tử trong set
b.remove(15)
# hoặc dùng hàm discard , pop , clear
b.discard(14)
print(b)

# Các phép toán trên tập hợp 
# Union : Phép hợp lấy ra các phần tử thuộc một trong 2 tập hợp sử dụng union hoặc | 
u = s | b
print(u)

# Intersection : Phép giao lấy ra các phần tử thuộc cả 2 tập hợp sử dụng intersection hoặc &
i = s & b
print(i)

# Difference : Phép hiệu lấy ra các phần tử thuộc tập hợp đầu tiên nhưng không thuộc tập hợp thứ 2 sử dụng difference hoặc -
d = b - s
print(d)

# Symmetric Difference : Phép hiệu đối xứng lấy ra các phần tử thuộc 1 trong 2 tập hợp nhưng không thuộc cả 2 sử dụng symmetric_difference hoặc ^
sd = s ^ b
print(sd)

# Kiểm tra xem tập hợp này có phải là tập con của tập khác hay không 
print(s.issubset(b)) 

# Kiểm tra xem tập hợp này có phải là tập cha của tập khác hay không
print(s.issuperset(b))