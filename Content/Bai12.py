# List Slicing 
# là một kỹ thuật có thể truy cập vào 1 khoảng các phần tử trong list thông qua toán tử
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