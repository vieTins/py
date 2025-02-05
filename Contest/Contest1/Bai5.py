ktu = input()
maAscii = ord(ktu) # hàm ord() trả về mã ascii của ký tự
if ktu == "z" or ktu == "Z":
    maAscii = 65 
    print(chr(maAscii).lower())
elif maAscii >= 65 and maAscii <= 90 or maAscii >= 97 and maAscii <= 122: 
    maAscii+= 1 
    print(chr(maAscii).lower())
else :
    print("not a letter")