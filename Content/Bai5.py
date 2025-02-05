# vòng lặp for và hàm range () 
# vòng lặp for 
    # for var in iterable (giống như là một list)
    #     statement 
    #     statement 
    # else   (nếu for chạy xong thì thực hiện else nếu cần)
    #     statement   

# hàm range() : sinh ra một dãy số và bạn sẽ sử dụng vòng for để duyệt qua từng số trong dãy đã sinh ra 
    # range(start , stop , step) 
a = range (1 , 10 , 2) ;
for i in a :
    print(i , end=' ') 
print() 

# Duyệt từ 0 đến 50 
for i in range(51) :
    print(i , end=' ')
print() 

# Duyệt ngược từ 50 đến 0
for i in range(51 , 0 , -1) :
    print(i , end=' ')
else : # else sẽ được thực hiện khi vòng lặp kết thúc
    print()
    print("vong lap da ket thuc")

# Cây lệnh break kết thúc vòng lặp ngay lập tức 
# câu lệnh continue được đùng để bỏ qua lần lặp hiện tại và quay trở lại luôn vòng lặp tiếp the0.
# Các câu lệnh bên dưới continue ở trong vòng lặp sẽ được bỏ qua 

# vòng for lồng nhau 
# mỗi vòng for bên ngoài thì toàn bộ vòng for con bên trong sẽ được thực hiện 
for i in range(3) :
    print("vong for ben ngoai la : " , i , end="\n") 
    for j in range(2) : 
        print("vong for ben trong la : " , j ,end="\n")
    