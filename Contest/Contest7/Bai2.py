from functools import cmp_to_key
class MatHang :
    def __init__ (self , maMH , tenMH , dvi , giaBan , giaMua) :
        # maMH ban đầu là MH0001 và tự động tăng sau mỗi lần tạo mới 
        self.maMH = str(maMH)
        while len(self.maMH) < 4 :
            self.maMH = '0' + self.maMH
        self.maMH = 'MH' + self.maMH    
        self.tenMH = tenMH 
        self.dvi = dvi
        self.giaBan = giaBan
        self.giaMua = giaMua

    def __str__ (self) :
        return self.maMH + ' ' + self.tenMH + ' ' + self.dvi + ' ' + str(self.giaBan) + ' ' + str(self.giaMua)+ ' '  + ((self.giaBan) - (self.giaMua))
    def getLoiNhuan (self) :
        return (self.giaBan) - (self.giaMua)
    def getMaMH (self) :
        return self.maMH
def cmp (a, b) :
    ln1 , ln2 = a.getLoiNhuan() , b.getLoiNhuan()
    if ln1 != ln2 :
        return ln2 - ln1
    else : 
        if a.getMaMH() < b.getMaMH() :
            return - 1
        else : return 1
if __name__ == "__main__" : 
    n = int(input()) 
    danhSachMatHang = [] 
    for i in range(n) :
        matHang = MatHang(i + 1 , input() , input() , int(input()) , int(input()))
        danhSachMatHang.append(matHang)
    # sắp xếp theo lợi nhuận 
    danhSachMatHang.sort(key = lambda x : x.getLoiNhuan() , reverse = True)