import math
def tongUoc(n) :
    sum = 0 ;
    for i in range(1, math.isqrt(n) + 1 ) :   # duyệt tới căn bậc 2 
        if (n % i == 0 ) : 
            sum+=i 
            if i != n // i :
                sum +=  n//i 
    return sum ;
def demUoc(n) :
    count = 0 ; 
    for i in range(1, math.isqrt(n) + 1 ) : 
        if (n % i == 0 ) : 
            count+=1
            if i != n // i :
                count +=1
    return count ;
# hàm main 
if __name__ == "__main__" : 
    print ("Nhap vao so n") 
    n = int (input())
    print ("So luong uoc la : " , demUoc(n) , end="\n")
    print ("Tong uoc la : " , tongUoc(n) , end="\n")