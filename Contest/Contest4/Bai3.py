if __name__ == "__main__" : 
    n = int(input()) 
    a = list(map( int , input().split()))
    ns = int(input())
    count = 0 
    while count < ns :
        se = int(input()) 
        param = int(input())
        if se == 1 :
            a.append(param)
            for x in a :
                print(x , end=" ")
            count += 1
            print()
        elif se == 2 :
            if param in a :
                a.remove(param) 
            for x in a :
                print(x , end=" ")
            count += 1
            print()
        elif se == 3 :
            if param in a :
                print("YES")
            else :
                print("NO")
            count += 1
            print()

