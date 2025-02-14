class SinhVien : 
    def __init__(self , maSv , tenSv , ngaySinh , lop , diem):
        self.tenSv = tenSv
        self.ngaySinh = ngaySinh
        self.lop = lop
        self.diem = diem
        self.ma = format(maSv , '03d')
    def chuanHoaNgaySinh(self) : 
        if self.ngaySinh[1] == "/" :
            self.ngaySinh = '0' + self.ngaySinh
        if self.ngaySinh[4] == "/" :
            self.ngaySinh = self.ngaySinh[:3] + '0' + self.ngaySinh[3:]
    def __str__(self) :
        return self.ma + ' ' + self.tenSv + ' ' + self.ngaySinh + ' ' + self.lop + ' ' + str(self.diem)

if __name__ == "__main__" : 
    n = int(input())
    for i in range(n) :
        sv = SinhVien(i + 1 , input() , input() , input() , float(input()))
        sv.chuanHoaNgaySinh()
        print(sv)
        