chuoi = "An:8.5, Binh:7.0, An:9.0, Cuong:6.5, Binh:8.0, Dung:7.5"
chuoi1 = chuoi.split(", ")
print(chuoi1)
chuoi3 = []
for i in chuoi1:
    ten,diem = i.split(":")
    chuoi3.append((ten,float(diem)))
print(chuoi3)
tenduynhat = set()
for ten, diem in chuoi3:
    tenduynhat.add(ten)
print(tenduynhat)
dsdiem =[]
for i in tenduynhat:
    tong = 0
    demso = 0
    for ten,diem in chuoi3 :
        if ten == i:
            tong += diem
            demso += 1
    kq = tong/demso
    dsdiem.append((ten,kq))
    print(f"{i} : {kq}")
print(dsdiem)
diemcaonhat = max([diem for ten,diem in dsdiem])
diemthapnhat = min([diem for ten,diem in dsdiem])
for ten,diem in dsdiem :
    if diem == diemcaonhat:
        print("diem cao nhat ")
        print(f"{ten} : {diem}")
    elif diem == diemthapnhat:
        print("diem thap nhat")
        print(f"{ten} : {diem}")
for i in range(len(dsdiem) - 1):
    for j in range(i + 1, len(dsdiem)):
        if dsdiem[i][1] < dsdiem[j][1]:
            a = dsdiem[j]
            dsdiem[j] = dsdiem[i]
            dsdiem[i] = a
        else :
            continue
print(dsdiem)


