# Kế thừa 
class Nguoi :
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def thongtin(self):
        print(f"Tên: {self.ten}, Tuổi: {self.tuoi}")
class SinhVien(Nguoi): # muốn kế thừa thì truyền vào class cha
    def __init__(self, ten, tuoi, mssv):
        super().__init__(ten, tuoi)
        self.mssv = mssv
    def thongtin(self):
        super().thongtin()
        print(f"MSSV: {self.mssv}")
# Đa kế thừa và kế thừa nhiều mức 

if __name__ == '__main__':
    sinhvien = SinhVien("Nguyễn Văn A", 20, "123456")
    sinhvien.thongtin() 