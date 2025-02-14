f1 = open("input.txt" , "r")
f2 = open("output.txt" , "w")
for name in f1 : 
    a = name.split() # tách chuỗi thành list
    name = " ".join(a).title() 
    f2.write(name + "\n")
f1.close()
f2.close()