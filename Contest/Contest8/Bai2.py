f1 = open(r"Contest\Contest8\input.txt" , "r")
f2 = open(r"Contest\Contest8\output.txt" , "w") # tham số r để tránh lỗi khi chạy trên linux
data = f1.read()
temp = "" 
a = [] 
for i in range(len(data)) :
    if data[i] != "," : 
        temp+= data[i]
    else : 
        a.append(temp)
        temp = ""
a.append(temp) # thêm phần tử cuối cùng vào list
for name in range(len(a)) : 
    a[name] = a[name].strip() 
    a[name] = a[name].title()
    f2.write(a[name] + ",")