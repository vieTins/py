# Nạp chồng toán tử cho Class 
# Hàm __add__ được sử dụng khi bạn cần nạp chồng toán tử + cho 2 đối tượng của một class 
# Hàm __sub__ được sử dụng khi bạn cần nạp chồng toán tử - cho 2 đối tượng của một class
# Hàm __mul__ được sử dụng khi bạn cần nạp chồng toán tử * cho 2 đối tượng của một class
# Hàm __truediv__ được sử dụng khi bạn cần nạp chồng toán tử / cho 2 đối tượng của một class
# Hàm __floordiv__ được sử dụng khi bạn cần nạp chồng toán tử // cho 2 đối tượng của một class
class SoPhuc () : 
    def __init__(self , thuc , ao):
        self.thuc = thuc
        self.ao = ao
    def __add__(self , other) :
        return SoPhuc(self.thuc + other.thuc , self.ao + other.ao)
    def __sub__(self , other) :
        return SoPhuc(self.thuc - other.thuc , self.ao - other.ao)
if __name__ == "__main__" : 
    sp1 = SoPhuc(1,2)
    sp2 = SoPhuc(3,4)
    sp3 = sp1 + sp2
    print(f'{sp3.thuc} + {sp3.ao}j')
        