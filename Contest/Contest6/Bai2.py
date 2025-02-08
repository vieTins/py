# tách từ 
if __name__ == "__main__":
    s = "nguyenviettin.python?java!c++"
    delim =".?!"
    for x in delim :
        s = s.replace(x, " ")
    print(s.split())