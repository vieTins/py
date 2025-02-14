# Lớp phân số 
from math import gcd
class phanSo :
    def __init__ (self , tu , mau) :
        self.tu = tu
        self.mau = mau
    def toi_gian (self) :
        ucln = gcd(self.tu , self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __str__ (self) :
         return f'{self.tu}/{self.mau}' # f' dùng để format string

if __name__ == "__main__" :
    tu , mau = map(int , input().split())
    p = phanSo(tu , mau)
    p.toi_gian()
    print(p)