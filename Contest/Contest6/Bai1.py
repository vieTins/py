# Tần suất xuất hiện của các kí tự trong xâu 
# C1 : Mảng đánh dấu 
def mangDanhDau (s) :
    cnt = [0] * 256 
    for x in s :
        cnt[ord(x)] += 1 
    for i in range (256) :
        if cnt[i] > 0 :
            print (chr(i) , cnt[i] , end='\n')
    # sẵp xếp theo thứ tự xuất hiện 
    for i in s :
        if cnt[ord(i)] > 0 :
            print (i , cnt[ord(i)] , end='\n')
            cnt[ord(i)] = 0
# C2 : Dict 
def countDict(s) :
     d = {}
     for x in s :
         if x in d :
                d[x] += 1
         else :
                d[x] = 1
     for x , y in d.items() :
            print (x , y , end='\n')
     for x in sorted(d) :
            print (x , d[x] , end='\n')
if __name__ == "__main__" :
    s = input()
    countDict(s)