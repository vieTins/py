from math import *
def nhapMang (n) : 
    a = list(map(int , input().split()))
    return a 
def check (a) :
    min_val = min(a)
    count = 0
    for i in a :
        if i == min_val:
            count += 1
    return count
    
if __name__ == "__main__" :
    n = int(input()) 
    a = nhapMang(n)
    print(check(a))