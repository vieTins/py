# vẽ hình 
n  = int(input())
for i in range(n) : 
    for j in range (n) :
        print ("*" , end = " ")
    print(" ")
print (" ")

for i in range(n) : 
    if (i == 0 or i == n - 1) :
        for j in range (n) :  
             print ("*" , end = " ") 
        print(" ")
    else :
        for j in range (n) : 
            if (j == 0 or j == n - 1) :
                print ("*" , end = " ")
            else :
                print (" " , end = " ")
        print(" ")
print(" ")

for i in range(n) : 
    if (i == 0 or i == n - 1) :
        for j in range (n) :  
             print ("*" , end = " ") 
        print(" ")
    else :
        for j in range (n) : 
            if (j == 0 or j == n - 1) :
                print ("*" , end = " ")
            else :
                print ("#" , end = " ")
        print(" ")
print(" ")

for i in range( 1 , n + 1 ) : 
    for j in range (1 , n +1) : 
        if (i == 1 or i == n or  j == 1 or j == n) : 
            print (i , end = " ")
        else :
            print (" " , end = " ")
    print(" ")