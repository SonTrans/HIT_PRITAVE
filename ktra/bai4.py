chuoisonguyen = input("nhap chuoi so nguyen (cach nhau boi dau cach) :")
list1 = list(map(int, chuoisonguyen.split()))
soluong = []
for i in range(len(list1)-2):
    demso = 0
    for y in range(i+1, len(list1) -1):
        demso += 1
        if list1[i] == list1[y]:
            soluong.append(demso)
print(soluong)
for i in soluong:
    if i == max(soluong):
        print(i)