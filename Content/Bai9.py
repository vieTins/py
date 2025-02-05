# hàm 
def tong(x ,y) :
    return x + y
# hàm tính giai thừa 
def tinhGiaiThua (n) :
    res = 1 ; 
    for i in range(1 , n+1) : 
        print(i) ;
        res *=i 
    return res 
def luyThua (a,b) :
    res =1  ;
    for i in range(b) : 
        print(i)
        res *= a ;
    return res ;
# có thể truyền không theo thứ tự tham số 
#  code để chạy chương trình 
# bắt đầu hàm main
if __name__ == '__main__' : 
    x, y = map(int , input().split())

    print(tong(x,y))
    print(tong(y= 10 , x = 30)) # có thể truyền không theo thứ tự tham số 
    print("Nhap vao so n : ") 
    n = int(input()) 
    print(tinhGiaiThua(n))
    print("Nhap vao so a va so mu b  : ") 
    a , b = map(int , input().split()) ;
    print(luyThua(a,b))

