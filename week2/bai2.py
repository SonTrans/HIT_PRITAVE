import math
n = int(input("nhap so nguyen n :"))
demso = 0
for i in range(1,n):
    if i == 1:
        continue
    elif i / math.sqrt(i) == int(math.sqrt(i)):
        demso = demso +1
    else :
        continue
print(f"vay tu 1 den {n} se co {demso} so chinh phuong neu khong tinh 2 dau mut")
