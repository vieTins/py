# Mảng đánh dấu : sử dụng chỉ số của mảng để đánh dấu 
# Giá trị khác nhau trong mảng : Tìm số lượng phần tử khác 
# Những bài toán liên quan đến tần suất xuất hiện 

if __name__ == "__main__" :
  a = [1,2,1,2,3,1,4,2 , 10 ]
  cnt = [0] * 10000001
  for x in a : 
    cnt[x] += 1 
  for x in a :
     if cnt[x] != 0 : 
         print(x , cnt[x])
         cnt[x] = 0
         
