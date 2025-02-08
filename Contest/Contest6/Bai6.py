if __name__ == "__main__" :
    s = input() + "#"
    dem , t = 1 , s[0] 
    res = 1 
    ans = s[0] 
    for i in range (1 , len(s)) :
        if s[i] == s[i-1] :
            dem+=1 
            t += s[i]
        else :
            if dem > res :
                res = dem 
                ans = t 
            elif dem == res :
                if t > ans :
                    ans = t 
            dem = 1
            t = s[i]
    print(ans)