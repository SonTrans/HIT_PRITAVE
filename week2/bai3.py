n = int(input("nhap so luong hoc vien: "))
ho_ten_list = []
for i in range(n):
    ho_ten = input(f"nhap ho ten hoc vien thu {i+1}: ")
    ho_ten_list.append(ho_ten)
diem1_list = []
for i in range(n):
    diem1 = int(input(f"nhap diem tx1 cua {ho_ten_list[i]}: "))
    diem1_list.append(diem1)
diem2_list = []
for i in range(n):
    diem2 = int(input(f"nhap diem tx2 cua {ho_ten_list[i]}: "))
    diem2_list.append(diem2)
hoc_vien_list = list(zip(ho_ten_list, diem1_list, diem2_list))
print("\ndanh sach hoc vien:")
for i, (ho_ten, d1, d2) in enumerate(hoc_vien_list, 1):
    tong = d1 + d2
    if tong == 200 :
        xephang = "xuat sac"
    if tong >= 150 and tong < 200:
        xephang = "gioi"
    if tong >= 100 and tong < 150 :
        xephang = "kha"
    if tong < 100 :
        xephang = "yeu"
    print(f"{i}. {ho_ten} - {tong} - {xephang}")
