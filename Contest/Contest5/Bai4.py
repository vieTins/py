# Check số thuận nghịch trong tam giác dưới 
def check(n) :
    res = n % 10 
    temp = n // 10
    while temp  != 0 :
        res = res * 10 + temp % 10
        temp //= 10
    return res == n

if __name__ == "__main__" :
    n = int(input())
    a = [] 
    for _ in range(n) :
        b = list(map(int , input().split()))
        a.append(b)
    count = 0 
    for i in range(n) :
        for j in range( i+ 1) :
            if check(a[i][j]) :
                count += 1
    print(count)