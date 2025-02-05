# Tuple là một collection có thứ tự trong python 
# Các phần tử có  thứ tự 
# không thể thay đổi , tức là không thể thêm xóa sửa
# Tạo tuple phải đưa các phần tử vào trong đóng mở ngoặc tròn 
a = (1,2,3) 
b = (1,)  # chỉ có một phần tử thì phải có dấu phẩy 
# tạo tuple thông qua constructor tuple () 
c = tuple([1,2,3])
print(c)
# giống như list nhưng không thể thay đổi được 
# tuple chứa list thì vẫn có thể thay đổi được 
d = ("28tech" , [1,2,3] , "java")
d[1][0] = 100 
print(a)

# Sắp xếp tuple 
#  Cách 1 :  Sử dụng hàm sorted sau đó convert ngược lại tuple 
e = (9,5,7,3,0,2) 
e = tuple(sorted(e)) 
print(e)

# Count và index 
# Hàm count đếm số lần xuất hiện của 1 pt trong tuple và index để trả về chỉ số đầu tiên của một pt trong tuple 
print (e.count(3)) 
print (e.index(3))

#  Kỹ thuật Unpacking
#  là một kthuat giúp tách một tuple , list , iterable ra thành biến rời rạc 
#  chú ý số lượng phần tử ở bên trái dấu bằng phải bằng số lượng phần tử của iterable bên phải dấu bằng 

userInfo = ("23NS094" , "NguyenVietTin" , "23NS2","QuangNam") 
idUser , nameUSser , classUser,_ = userInfo 
print(idUser , nameUSser ,classUser)
# đối với các biến không cần phải lấy thông tin thì dùng dấu gạch dưới 

# Unpacking với vòng for 
studentInfo = ((1 , "Tin") , (2 , "Tuan") , (3, "Phuoc"))
for x , y in studentInfo : 
    print(x , " -> " , y)

# Nếu như iterable bên phải dấu bằng có quá nhiều phần tử , trong khi đó 
# chỉ muốn lấy ra một vài phần tử => dùng toán tử * 
number =(1,2,3,4,5,6) 
x , y , *z = number   # lấy hai phần tử là x , y còn *z là các phần tử còn lại thì không lấy 
print(x,y)
print(z)  # là list các phần tử còn lại 