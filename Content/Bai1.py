# câu lệnh print 
# cú pháp :
# print(object , sep = seperator , end = end) ;
# Object : các đối tượng trong Python 
# Sep : Phân cách giữa các đối tượng khi in , nếu không có tham số này thì mặc định sẽ là dấu cách 
# End : Chỉ ra kí tự  được in ở cuối của dòng , nếu không có tham số này thì mặc định sẽ là dấu cách 
a = 100 ;
b = 200 ;
c = 300 ;       
print (a , b,c) ;
print("nguyen viet tin") ; 
# print có tham số sep 
print (a , b, c , sep='/' , end='!\n')  
print (type(a)) 
#  kiểu dữ liệu số phức 
soPhuc = 50+9j 
print ("Kieu du lieu cua bien soPhuc la : "  , type(soPhuc))
#  in số thực với lượng chữ số sau dấu phẩy xác định 
numberA = 28.19223443 
print ('%.2f' %numberA) 
print (round(numberA , 2))  # làm tròn 
print ('{:.2f}'.format(numberA))
# số phức gồm phần thực (real part) và phần ảo (imaginary part) đi kèm j 
# có thể trích xuất phần thực bằng x.real và  phần ảo bằng x.imag
print(soPhuc.real) 
# các giá trị được xác định là true trong python ; xâu khác rỗng , các số khác 0
# ép kiểu 
# sử dụng các hàm như int() , float() , str() , complex() để ép kiểu
