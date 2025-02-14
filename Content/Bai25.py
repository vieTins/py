# Xử lý File 
# Để cods thể thao tác với file , trước hết cần mở file và xác định mode mở 
# r : đọc file
# w : ghi file
# a : ghi thêm vào file
# x : tạo file mới
# Ngoài ra chỉ rõ dạng làm việc với file text hay file nhị phân bằng cách thêm t hoặc b vào cuối mode mở 
# Nếu muốn đọc từng dòng trong file thì sử dụng hàm readlines()
import os
f = open("Content/test.txt" , "r")
print(f.read()) # đọc toàn bộ file 

for lines in f :
    print(lines) # đọc từng dòng trong file

f.close() # đóng file

# Để ghi vào file thì sử dụng hàm write() 
# Khi mở file với mode w và a sẽ tạo file mới nếu chưa tồn tại 
f = open("Content/test.txt" , "a")
f.write("Hello World")
f.close()

# Để xóa file sử dụng hàm os.remove()
os.remove("Content/test.txt") # xóa file test.txt
