# nhập dữ liệu từ bàn phím 
a = input("Nhap vao mot chuoi ") ;
print("chuoi vua nhap la : " , a) ;
# nếu muốn nhập số thì phải ép kiểu

# nhập nhiều số 
b = input("Nhap vao 3 so : ") ;
c = b.split() ; # tách chuỗi thành mảng
x , y , z = map(int , c) ;  # ép kiểu 
# map là hàm dùng để ánh xạ mỗi phần tử của mảng c với hàm int
print(x, y,z) ;

# nhập 4 số nguyên trên 1 dòng 
d = input("Nhap vao 4 so nguyen : ") ;
m, n , p , q = map(int , d.split()) ;
print(m,n,p,q) ;