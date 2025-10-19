ten = input("Nhập tên : ")
tuoi = int(input("Nhập tuổi : "))
Gtinh = input("Nhập giới tính (Nam/Nữ) : ")
Ny = input("bạn có Ny chưa (Roi/Chua) : ")
if (Ny != "Roi" and Ny != "Chua") :
    Ny = "Chua"
print(f"Tên : {ten}")
print(f"Tuổi : {tuoi}")
print(f"Giới tính : {Gtinh}")
print(f"Tình trạng hôn nhân : {Ny}")
if (Gtinh == "Nữ" and Ny == "Chua"):
    print("+1 đối tượng cho bạn Hùng")
