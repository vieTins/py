n = int(input()) 
for i in range(n) : 
    for j in range( i + 1) : 
        print ( "*" , end = " ")
    print(" ")
print (" ")
for i in range(n , 0 , -1) : 
    for j in range (i) : 
        print("*" , end = " ")
    print(" ")
print(" ")

for i in range (1 , n+1) :
    for j in range (1 , n  +1)  :
        if j <= n - i: 
            print(" " , end = " ")
        else : 
            print ("*" , end = " ")
    print(" ")
print(" ")

for i in range (1 , n+1) :
    for j in range ( 1 , n +1 ) : 
        if j >= i :
            print ("*" , end = " ")
        else : 
            print (" " , end = " ")
    print(" ")
print(" ")

for i in range (1 , n + 1) : 
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n or i == 1 :
            print ("*" , end = " ")
        else :
            print (" " , end = " ")
    print(" ")
print(" ")
