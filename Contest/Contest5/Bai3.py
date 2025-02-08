if __name__ == "__main__" :
    n , m = map(int , input().split())
    a = [] 
    for _ in range(n) :
        b = list(map(int , input().split()))
        a.append(b)

    minValue  , maxValue = 10 ** 9 , -10 ** 9
    for i in range (n) :
        minValue = min(minValue , min(a[i]))
        maxValue = max(maxValue , max(a[i]))

    print(minValue)
    for i in range(n) :
        for j in range(m) :
            if a[i][j] == minValue :
                print(i + 1, j + 1)
    print(maxValue)
    for i in range(n) :
        for j in range(m) :
            if a[i][j] == maxValue :
                print(i + 1, j + 1)