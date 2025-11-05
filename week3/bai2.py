chuoi = (input("Nhập chuỗi : "))
chuoi1 = ""
for i in chuoi :
    if i.isalnum() or i == " ":
        chuoi1 += i
xoa = chuoi1.strip()
a = ""
for i in xoa :
    if i.isalnum() :
        a += i
demnguyenam = 0
if "e" in xoa.lower():
    demnguyenam += xoa.lower().count("e")
if "u" in xoa.lower():
    demnguyenam += xoa.lower().count("u")
if "o" in xoa.lower():
    demnguyenam += xoa.lower().count("o")
if "a" in xoa.lower():
    demnguyenam += xoa.lower().count("a")
if "i" in xoa.lower():
    demnguyenam += xoa.lower().count("i")
demphuam = len(a) - demnguyenam
tachchuoi = xoa.split()
daochuoi = [i[::-1] for i in tachchuoi]
dx = xoa[::-1]
print(f"Xóa các kí tự đb và khoảng trắng 2 đầu : {xoa}")
print(f"Viết thường hết các kí tự : {xoa.lower()}")
print(f"Nguyên âm: {demnguyenam}, Phụ âm: {demphuam}")
print(daochuoi)
if dx == xoa :
    print(True)
else : 
    print(False)

