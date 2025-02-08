if __name__ == "__main__" :
    s = input() 
    a = s.split()
    d = {} 
    for x in a :
        if x in d :
            d[x] += 1
        else :
            d[x] = 1
    min_fre , max_fre = 1e9 , 0
    res1 , res2 = "" , ""
    for x in sorted(d) :
        if d[x] <= min_fre :
            min_fre = d[x] 
            res1 = x 
        if d[x] >=   max_fre :
            max_fre = d[x]
            res2 = x
    print (res1 , max_fre , end='\n')
    print (res2 , min_fre , end='\n')        