from collections import Counter 
if __name__ == "__main__" : 
    n = int(input()) 
    a = list(map(int , input().split()))
    b = list(dict(Counter(a)).items())
    c = sorted(b , key = lambda x : x[0])
    for val , fre in c :
        print(val , fre)
    print() 
    for val , fre in b :
        print(val , fre )