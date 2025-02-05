# 3 vỏ bia thì đổi được 1 chai bia 
# 1 chai bia hết 28 xu 
# n xu thì mua được tối đa bao nhiêu 
n = int(input())
tongbia = n // 28 
vo = tongbia 
while vo >= 3 :
    temp = vo // 3 
    tongbia += temp 
    vo = vo % 3 + temp 
print(tongbia)