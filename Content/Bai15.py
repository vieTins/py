# Map () là một hàm có chức năng apply một hàm có sẵn cho mọi phần tử trong 1 iterable (list , tuple , str)
# Map (function , iterable)  =>> giá trị trả về một đối tượng thuộc lớp map . Nên ép sang list 
# với function sẽ là hàm được áp dụng 
from math import *
import math
def newPow (a) :
    return a * a 
a = [1,2,3,4,5,6] 
a = list(map(newPow , a)) # áp dụng cho toàn bộ 

# áp dụng map vói nhiều iterable 
def add (a,b) : 
    return a + b
def prime (n) :
    for i in range(2 , math.isqrt(n) + 1):
        if n % i == 0 :
            return False 
        return n > 1 
if __name__ == "__main__" : 
    a = [1,2,3,4] 
    b = [4,5,6,7] 
    c = list(map(add , a , b))
# áp dụng map với nhiều iterable sử dụng lambda 
    d = list(map(lambda x , y : x + y , a, b))
    print(d)

# filter() được sử dụng để trích xuất các phần tử trong một iterable khi apply một hàm nào đó 
# với phần tử đó mà hàm trả về giá trị là True 
    e = list(filter(prime , a))
# Dùng List_Comprehension
    f = [x for x in a if prime(x)]
# Áp dụng filter với lambda 
    g = list(filter(lambda x : x % 2 != 0 , a))
    print(e)