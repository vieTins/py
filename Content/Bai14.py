# List_Comprehension 
# là một cách nhanh chóng để có thể tạo một ctdl từ iterable 
# kết hợp đkien và vòng lặp đê rút gọn cú pháp 
# cú pháp 
# [Expression for var in iterable]
a = [1,2,3,4]
b = [x + 3 for x in a]
print(b)
c = [x **3 for x in range(1,11)]
print(c)
# có thể kết kết hợp với md if 
d = [x **3 for x in range(1,11) if x > 4]
print(d)

# khi sử dụng các hàm có sẵn thì sử dụng map sẽ nhanh gọn hơn so với list_comp 
# tuy nhiên khi apply một hàm khác các hàm có sãn thì sự kết hợp list_comp với lambda sẽ ngắn gọn hơn 