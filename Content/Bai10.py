# Đệ quy - Hàm gọi lại chính nó 
# Bài toán con nhỏ nhất và Công thức truy hôì 
# Stack - push và pop 
def A():
    print("A")
    A() # Đệ quy 
def B() :
    A() 
    print("B") 
# hàm đệ quy để tính tổng từ n - 0 
def sum (n) :
    if n == 0 :
        return 0 
    else :
        return n + sum (n-1) 
# từng hàm được đẩy vào ngăn xếp -> B() A()
if __name__ == "__main__" :
    print(sum(4))