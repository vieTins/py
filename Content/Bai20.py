# Dictionaries là một ctdl thuộc dạng associative array hay hashmap
# Có dạng key : value
# Để tạo dict cần liệt kê các cặp key : value trong dấu {} phân tách bởi dấu , 
from collections import Counter
infor = {
    "name" : "Nguyen Van A",
    "age" : 20,
    "address" : "Ha Noi"
}
# Có thể tạo bằng cách convert cặp 2 giá trị thành một item của dict  , giá trị thứ 1 làm key , giá trị thứ 2 làm name 
infor2 = dict([("name","Nguyen Van A"),("age",20),("address","Ha Noi")]) 
print(infor2)

# tạo bằng hàm zip
keys = ["name" , "age" , "address"]
values = ["Nguyen Van A" , 20 , "Ha Noi"]
infor3 = dict(zip(keys , values))

# tạo bằng hàm fromkeys
a = dict.fromkeys(["name" , "age" , "address"] , "Unknown") 
print(a)

# Key phải là object không thể thay đổi nhưng value có thể thay đổi
# Để truy cập vào value thì dùng key
print(infor["name"])

# hoặc dùng hàm get 
print(infor.get("name"))

# Để lấy key , value , item trong dict 
print(list(infor.keys()))
print(list(infor.values()))
print(list(infor.items()))

# Thêm một item vào dict
infor["phone"] = "0123456789"

# Xóa item thì dùng hàm pop hoặc del 
infor.pop("phone")
del infor["name"] 

# Bài tập liên quan tới các gía trị khác nhau trong mảng , tìm kiếm nhanh
# VD : Đếm tần suất xuất hiện của các phần tử trong mảng

# sử dụng counter để đếm 
def count_elements (a) :
    b = list(dict(Counter(a)).items())
    return b 
if __name__ == "__main__" :
    a = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,1,2,3,4,1,2,3,1,2] 
    d = {}
    for x in a :
        if x in d :
            d[x] += 1 
        else :
            d[x] = 1 
    b = list(d.items()) 
    b.sort(key = lambda x :x[0])  #sắp xếp theo key 
    print(b)

# dict comprehension là một cách nhanh gọn giúp tạo ra một dict từ một iterable
# {key : value for var in iterable}

a = [1,2,3,4,5,6,7,8,9] 
d2 = {x : x ** 2 for x in a}
print(d2)

