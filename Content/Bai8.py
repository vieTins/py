# Tuple 
# Cũng là một cấu trúc mảng , tương tự như cấu trúc List 
# khác nhau là sử dụng dấu ngoặc () , và một tuple được khai báo rồi thì không thay đổi được giá trị 
# khong hỗ trợ các phương thức append() , pop()
myTuple = ('viet' , 'tin')
print (myTuple)

# Dictionary 
# Cũng là một cấu trúc mảng , nhưng các phần tử bao gồm key và value 
# Khai báo bằng cặp dấu ngoặc {}
myDic = {1:'I' , 6:'Love' , 9:'You'}
print(myDic)
print(myDic[6])
# thêm một phần tử
# dic[key] = value ;
myDic[10] ="Very Much"
# xóa toàn bộ dl 
# myDic.clear() 
# trả về một bản copy của đối tượng 
# myDic.copy() 
# Tạo đối tượng mới từ seq và giá trị là value 
seq = ("Key1 " , "Key2 " , "Key3") 
val = (1,2,3) 
newMyDict = dict.fromkeys(seq , val) ; # key1 =(1,2,3) 
print(newMyDict)

# kiểm tra một key có tồn tại hay không 
print('Key1 ' in newMyDict)

# trả về một list chứa các Key
myKey= newMyDict.keys() 
print(myKey)
myValue = newMyDict.values() ;
print(myValue)