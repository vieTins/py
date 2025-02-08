from math import *
def nt(n) :
    if n < 2 :
        return False
    for i in range( 2 , isqrt(n) + 1) :
        if n % i == 0 :
            return False
    return True

if __name__ == "__main__" :
    n , m = map(int , input().split())
    a = [] 
    for _ in range(n) :
        b = list(map(int , input().split()))
        a.append(b)
    
    for i in range(n) :
        for j in range(m) :
            if nt(a[i][j]) :
                print(a[i][j] , end = " ")
        print()