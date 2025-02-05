# vòng lặp while , break , continue 
# thực hiện lặp vô thời hạn đến khi một điều kiện cụ thể được đáp ứng . chưa biết trước số lần lặp 
# while condition :
#     # code
# else :
#     # code 
count =  0 
while (count < 9 ) : 
    print("The count is : " , count , end='\n') 
    count+=1  
print ("Good bye" )

# khai báo hàm
# def functionName  (param , pram2 , ...) :
#     statements
# hàm nếu không trả về dữ liệu thì mặc định sẽ trả về giá trị None 

def demChuSo (n) :
    count =  0 
    while n != 0 :
        n //= 10 
        count += 1
    return count


def sum (a, b) :
    return a + b 

print ("Sum : " , sum(3,4) , end='\n')
# hàm có hỗ trợ giá trị mặc định cho tham số  khi không truyền vào
def plus (a, b = 5) :
    return a + b 

print ("plus : " , plus(3) , end='\n')

#  có thể thay đổi vị trí tham số khi gọi hàm  
print ("Sum : " ,sum (b = 7 , a = 10) , end='\n')

# Xử lý chuỗi 
str1 = "length" 
str2 = 'nguyenviettin'

# truy xuất từng ký tự trong một chuỗi theo hình thức index  str[1]
# dùng 3 dấu phẩy để khai báo trên nhìu dòng 
# Trích xuất chuỗi con [start:end]

print (str1[0:4],end="\n") 

# độ dài chuỗi 
count = len ("nguyenviettin")
print(count , end="\n")

# tìm và thay thế nỗi dung 
str2New = str2.replace("ng" , "NG");
print("chuoi moi la str2 " , str2New , end="\n")

# tìm chuỗi con 
str3 = "Hello World" 
print (str3.find("World" , 0 , 5)) 
# rfind

# tách chuỗi
print (str3.split(' '))
#  sử dụng hàm splitlines() để tách chuỗi theo từng hàng và loại bỏ ký tự newLine 
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

# trim ký tự khoảng trắng 
# loại bỏ các ký tự (mặc định là lý tự khoảng trắng) trước và sau 
newStr = "/nguyenviettin/" 
print(newStr.strip("/"))