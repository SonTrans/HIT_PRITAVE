chuoi1 = "Chao mung den CLB Tin Hoc HIT"
print(chuoi1)
chuoi2 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
print(chuoi2 + " 10 điểm")
for i in chuoi2 :
    if i.isupper():
        print(i, end = " ")
print()
for i in chuoi2 :
    if i.islower():
        print(i, end = " ")
print()
if ("CNTT" in chuoi2):
    print("Yes")
else :
    print("No")
kq = ""
for i in chuoi2:
    if i.isupper():
        kq += i.lower()
    elif i.islower():
        kq += i.upper()
    else :
        kq += i
print(kq)