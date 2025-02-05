# List 
number= [1,2,3,4]
names =['Mary', 'Peter'] 
# truy xuất từng phần tử của mạng bằng index , phần tử đầu tiên có thứ tự là 0

# kiểm tra theo giá trị 
print (1 in number) 
print ('Marry' not in names)

# trích xuất mảng con 
# [start:end]
print (number[0:3])

# xóa phần tử của mảng 
# thông qua tóan tử del 
del number[len(number)-1 ]
print(number)
# xóa trong một khoảng range

# Nối 2 mảng => dùng toán tử +
newList= number + names 
print(newList)

# thêm một phần tử vào mảng 
newList.append("Nguyenviettin")
print(newList)

# lấy phần tử cuối cùng
print (newList.pop())

# tìm một giá trị trong mảng 
print ("index of Mary: " , newList.index("Mary"))

# đảo ngược giá trị của mảng
newList.reverse() ;
print(newList)

# sắp xếp gía trị của phần tử 
newList.sort()

