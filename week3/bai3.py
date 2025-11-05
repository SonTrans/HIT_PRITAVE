chuoi = input("Nhap chuoi : ").lower()
chuoi1 = chuoi.split()
chuoi2 = chuoi1.copy()
i = 0
while i < len(chuoi1):
    j = i + 1
    while j < len(chuoi1):
        if chuoi1[i] == chuoi1[j]:
            del chuoi1[j]
        else:
            j += 1
    i += 1
print(chuoi1)
tansuat = []
dodaikitu = []
for i in (chuoi1):
    print(f"{[i]} co {(chuoi2).count(i)} so lan xuat hien")
    tansuat.append(chuoi2.count(i))
    dodaikitu.append(len(i))
for i in chuoi1:
    if len(i) == max(dodaikitu):
        print(f"tu dai nhat la : {i}")
for i,j in zip(chuoi1,tansuat) :
    if j == max(tansuat):
        print(f"phan tu {i} co so lan xuat hien nhieu nhat la {j}")
chuoi3 = []
for i in chuoi2 :
    if i.isalnum() :
        chuoi3 += i
print(f"do dai chuoi : {len(chuoi3)}")
for y in range(len(chuoi1) - 1):
    for j  in range(y+1,len(chuoi1) ):
        if len(chuoi1[y]) < len(chuoi1[j]):
            a = chuoi1[j]
            chuoi1[j] = chuoi1[y]
            chuoi1[y] = a
        else :
            continue
print(chuoi1)

