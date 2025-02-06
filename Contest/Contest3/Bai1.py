def nhapMang (n) : 
    a = list(map(int , input().split()))
    return a 
def check (a): 
     countLe , countChan , sumLe , sumChan = 0 , 0 , 0 , 0
     for i in range(len(a)) : 
        if (a[i] % 2 == 0) :
            countChan += 1 
            sumChan += a[i]
        else : 
            countLe += 1 
            sumLe += a[i]
     return countLe , countChan , sumLe , sumChan
      


if __name__ == "__main__" :
    n = int(input()) 
    a = nhapMang(n)
    countLe , countChan , sumLe , sumChan = check(a) 
    print(countLe , countChan , sumLe , sumChan)