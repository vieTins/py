# Hướng đối tượng 
# hàm init là hàm khởi tạo (như constructor) ở các nn khác , khởi tạo thông tin ban đầu
# tham số self trong python tương đương this trong java , là tham số đầu tiên của mọi phương thức
# trong python , mọi thuộc tính đều là public , không có private , protected
# dấu __ ở đầu tên thuộc tính là private , không nên truy cập trực tiếp
# dấu _ ở đầu tên thuộc tính là protected , không nên truy cập trực tiếp
class person :
    nationlity = 'Vietnam' # thuộc tính của lớp , thuộc tính chung
    def __init__(self , name , job):
        self.name = name
        self.__job = job # thuộc tính private
    def say(self):
        print('Hello , my name is ', self.name)
    def work(self):
        print('I am a ', self.__job)
if __name__ == "__main__":
    bob = person('Bob Smith' , 'developer')
    bob.say()
    bob.work()
