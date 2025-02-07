# Mảng 2 chiều 
# Để sử dụng mảng 2 chiều hay nhiều chiều ta sử dụng nested list

# Tạo mảng 2 chiều
if __name__ == "__main__" :
    n , m = map(int , input().split())
    a = []
    for i in range(n) : 
        b = list(map(int , input().split()))
        a.append(b)
    print(a)

# dùng list comprehension
b = [[0 for _ in range (m)] for _ in range(n)] 
# Tạo một list con gồm m phần tử đều là 0 rồi lặp lại n lần để tạo ra n hàng , mỗi hàng có m cột 

# Duyệt mảng 2 chiều
for i in range(n) :
    for j in range(m) : 
        print(a[i][j] , end = " ")
    print()

# Flatten mảng 2 chiều thành mảng 1 chiều 
c = [x for row in a for x in row]
print(c)