if __name__ == "__main__" :
    s = input() 
    a = s.split() 
    a.sort() 
    print (" ".join(a) , end='\n')
    a.sort(key = lambda x : (len(x) , x))  
    print (" ".join(a) , end='\n')