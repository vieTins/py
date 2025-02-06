# Xây dựng hàm so sánh cho hàm sort bằng cmp to key 
from functools import cmp_to_key
# -1 1 0
# Nếu a là thằng đứng trước , b là thằng đứng sau sau khi sắp xếp xong 
# Nếu a và b đã đúng thứ tự mà mình muốn thì trả về -1 , ngược lại trả về 0 

# sắp xếp các phần phần từ trong list theo thứ tự tổng chữ số tăng dần , nếu 2 số có cùng tổng chữ số thì số nhỏ hơn xếp trước 

def tong(n) :
    res = 0 
    while n != 0 :
        res += n % 10 
        n //= 10
    return res
def cmp (a,b) :
    tong1 , tong2 = tong(a) , tong(b)
    if tong1 != tong2 :
        return tong1 - tong2
    else : 
        return a - b
    
a = [123, 234, 345, 456, 567, 678, 789, 890, 999]
a.sort(key = cmp_to_key(cmp))
print(a)