if __name__ == "__main__" :
    n , m = map(int , input().split())
    a = [] 
    for _ in range(n) :
        b = list(map(int , input().split()))
        a.append(b)
    for i in range(n) :
        print(sum(a[i]) , end = " ")
    for j in range(m) :
        s = 0
        for i in range(n) :
            s += a[i][j]
        print(s , end = " ")

        