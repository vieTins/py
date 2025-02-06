def nhapMang (n) : 
    a = list(map(int , input().split()))
    return a  
def check (a , k) :
    count = 0 
    for i in range(len(a)) : 
        for j in range (i + 1 , len(a)) : 
            if a[i] + a[j] == k : 
                count+=1
    return count

if __name__ == "__main__" :
    n = int(input())
    a = nhapMang(n)
    k = int(input())
    print(check(a , k))