n = int (input())
dem = 1 
for i in range (1, n+1) :
    for j in range(1 , n+1) : 
       print (dem , end = " ")
       dem+=1 
    print(" ")
print(" ")

for i in range(1 , n+1 ) : 
    for j in range ( i  , n + i) : 
        print (j , end = " ")
    print(" ")
print(" ")

for i in range(1 , n+1 ) :
    for j in range (1 , n +1) : 
        if j <= n - i :
            print ("~" , end = " ")
        else :
            print (i , end = " ")
    print(" ")
print(" ")

for i in range(1 , n+1 ) :
    kc = n - 1 
    ktao = i 
    for j in range (i) : 
        print (ktao, end = " ") 
        ktao += kc 
        kc -= 1
    print(" ")