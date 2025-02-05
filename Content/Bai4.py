# các hàm phổ biến 
import math
# cách hai 
from math import *    # dùng mà kh cần math.
# print(help(math))
print(sqrt(36))  
print(isqrt(36)) # hàm này căn bậc hai nhưng chỉ lấy phần nguyên
# ceil :  làm tròn lên
print (ceil(3.2))
# floor  : làm tròn xuống
print (floor(3.2))
# factorial : giai thừa
print(factorial(5))
# gcd (a,b) : ucln 
print(gcd(12,18))
# comb (n,k) : tổ hợp chập k của n
print(comb(5,2))
# perm (n,k) : hoán vị chập k của n 
print(perm(5,2))
# hàm max 
print(max(1,2,3,4,5))
#hàm sum 
print(sum([1,2,3,4,5]))


# if else 
# các câu lệnh bên trong if được thụt lề so với if 
a = 10 
b = 20 
if a > 20 :
    print("Hello")
elif b >40:
    print("Bye")
else :
    print("Let's go")

# toán tử ba ngôi 
rs = "a" if a > b else "b"
# variable = statement if condition else statement


if a > b :
    max = a 
else :
    max = b 
print(max)

