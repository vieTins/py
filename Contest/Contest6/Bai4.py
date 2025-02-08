def check(n) :
    t = n[::-1] 
    return n == t
if __name__ == "__main__" :
    s = input() 
    a = s.split()
    se = set()
    b = []
    for x in a :
        if check(x) and x not in se :
            b.append(x)
            se.add(x)
    b.sort(key = lambda x : len(x)) 
    print (" ".join(b) , end='\n')
