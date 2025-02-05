# Lamda
# Lamda là một cách đơn giản để định nghĩa một hàm trong py
# định nghĩa hàm vô danh , một hàm không cần tên . Xây dựng một hàm chỉ bao gồm 1 câu lệnh 

# Lamda không thể chứa các câu lệnh : vidu như return , assest , pass
# Lamda chỉ chứa một biểu thức duy nhất 
# IIFE : Biểu thức lamda có thể được gọi ngay lập tức 
# Cú pháp : 
# Lambda parameters : expression 
func = lambda x : x ** 3  # có tham số là x và trả về x mũ 3 
print (func(10))
print ((lambda x : x ** 3)(10)) # IIFE  : gọi ngay lập tức 

# có thể kết hợp if else trong lambda 
findMax = lambda x, y : x if x > y else y 
print (findMax(100,200))
a = [-1 , 1 , 0  ,-5 , 9]
change = lambda l :  [x for x in l if x >=0]
print(change(a))

flatten = lambda big_list : [item for small_list in big_list for item in small_list] 
a = [[1,2,3] , [4,5,6] , [7,8,9]]
print(flatten(a))