from sys import stdin, stdout
class SinhVien :
    def __init__ (self ,ma , ten , lop , email)  :
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.email = email
    def getMa (self) :
        return self.ma
    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + self.lop + ' ' + self.email

if __name__ == "__main__" : 
    a = [] 
    lines = [] 
    for x in stdin : 
        lines.append(x)
    for i in range(0 , len(lines) , 4) : 
        sv = SinhVien(lines[i].strip() , lines[i + 1].strip() , lines[i + 2].strip() , lines[i + 3].strip())
        a.append(sv)
    a.sort(key = lambda x : x.getMa())
    for x in a :
        print(x)
    