# phân tích thừa số nguyên tố 
from math import * 
def pt (n) :
    for i in range ( 2, isqrt(n) + 1) : 
        if n % i == 0  : 
            while n % i == 0 : 
                print (i , end = " x ")  
                n //= i 
    # nếu n là snt 
    if n > 1 :
        print (n)
if __name__ == "__main__":
    n = int(input())
    pt(n)
    