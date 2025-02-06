def nhapMang (n) : 
    a = list(map(int , input().split()))
    return a   
def check (a) :
    temp = [0] * 1001
    for i in a :
        if temp[i] == 0 :
            print(i , end = " ")
            temp[i] = 1

if __name__ == "__main__" :
    n = int(input())
    a = nhapMang(n)
    check(a)