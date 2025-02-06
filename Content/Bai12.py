# List Slicing 
# là một kỹ thuật có thể truy cập vào 1 khoảng các phần tử trong list thông qua toán tử
# a [start : end : step] 

# nếu không có start thì mặc định là 0
# nếu không có end thì mặc định là len(a) - 1 
# nếu không có step thì mặc định là 1
# nếu step là số âm thì bắt đầu từ phần tử cuối cùng

myList = [1,2,3,4,5,6] 
myListSlicing = myList[2 : 5 : 1]  # cận trên không lấy 
print(myListSlicing)
print() 
# lật ngược list
myListSlicing = myList[::-1]
print(myListSlicing)
print() 
# thay đổi giá trị của nhiều phần tử trong một đoạn 
myList[2:5] =  ["ngueynviettin"]
print(myList)
print() 
# xâu rỗng thì xóa 
# copy một list
myCopyList = myList[:]
print(myCopyList)
print(myCopyList is myList) 
print(myCopyList ==  myList) 