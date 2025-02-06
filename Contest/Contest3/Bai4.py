def nhapMang (n) : 
    a = list(map(int , input().split()))
    return a  
def check (a) :
    lech_min = 10 ** 18 
    for i in range(len(a)) : 
        for j in range (i + 1 , len(a)) : 
            if abs(a[i] - a[j]) <  lech_min : 
                lech_min = abs(a[i] - a[j])
    return lech_min

if __name__ == "__main__" :
    n = int(input())
    a = nhapMang(n)
    print(check(a))