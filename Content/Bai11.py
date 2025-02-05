# Lits tương tự như cấu trúc dl mảng ở các ngôn ngữ lập trình khác 
# - Có thứ tự 
# - Truy cập thông qua chỉ số 
# - Có thể chứa các Object thuộc các kiểu dl khác nhau 
# - Các phần tử có thể thay đổi giá tri , các thao tác thêm , xóa 

myList = ['nuyenviet' , 1 , 2, 3 +5j]  # nhiều kiểu dl 

# List constructor  - tạo ra list
s = "nguyenviettin" 
a = list(s)
print(a)
# list hỗ trợ chỉ sổ âm
#  - 1 là phần tử cuối cùng trong mảng 
for i in range(0 , len(a)): 
    print(a[i] , end =' ')
print() 
    
# for each 
for item in a :
    print(item , end=" ")
print() 

# thêm một phần tử vào cuối 
myList.append("_nviettin")
# thêm vào vị trí bất kì 
myList.insert(1 , '23NS094')
for item in myList :
    print(item , end=" ")
print() 

# hàm pop sẽ xóa phần tử thông qua chỉ số 
# nếu không thêm chỉ số thì sẽ xóa pt cuối cùng
# hàm pop trả về phần tử mà nó xóa khỏi list 
myList.pop(2)
# hàm del cũng như pop nhưng không trả về pt bị xóa 

# hàm remove thì xóa theo giá trị truyền vào -> nếu có nhiều giá trị giống nhau thì xóa đi phần tử đầu tiên 
# nếu không có thì dùng remove sẽ báo lỗi 
# hàm clear xóa hết 

# sao chép list 
# giúp nhân bản nội dung của list ban đầu 
myCopyList = myList *2 
for item in myCopyList :
    print(item , end=" ")
print() 
# tạo list chứa 1000 phần tử là số 0 
zeroList = [0] * 1000 
# Combine List - Nối list   
myList.extend(myCopyList) 
myList+=myCopyList 