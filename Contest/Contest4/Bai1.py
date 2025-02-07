if __name__ == "__main__" : 
    n = int(input()) 
    a = list(map(int , input().split()))
    a = set(a) 
    q = int(input())
    for _ in range(q) :
        x = int(input())
        if x in a :
            print("YES")
        else :
            print("NO")
