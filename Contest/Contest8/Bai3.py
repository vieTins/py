f1 = open(r"Contest\Contest8\input.txt" , "r")
f2 = open(r"Contest\Contest8\output.txt" , "w")

def email(s) :
    a = s.lower().split() 
    res = a[-1].lower()
    for x in a[:-1] :
        res += x[0] 
    res += "@vku.udn.vn" 
    return res 

def password(s) :
    a = s.split("/")
    res = "" 
    for x in a : 
        res += str(int(x))
    return res  

data = []
for lines in f1.readlines() :
    data.append(lines.strip())
for i in range(0 , len(data) , 2) :
    f2.write(email(data[i]) + "\n")
    f2.write(password(data[i + 1]) + "\n")

f1.close()
f2.close()