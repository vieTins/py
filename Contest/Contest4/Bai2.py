if __name__ == "__main__" : 
    n = int(input()) 
    a = list(map (int , input().split())) 
    s = set() 
    for x in a :
         if x not in s :
            print(x , end=" ")
            s.add(x)
        
          