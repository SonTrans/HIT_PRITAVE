while True :
    ngay = int(input("nhap ngay sinh : "))
    thang = int(input("nhap thang sinh : "))
    if thang < 1 or thang > 12 :
        continue
    if thang in [1,3,5,7,8,10,12]:
        max = 31
    if thang in [4,6,9,11] :
        max = 30
    if thang == 2:
        max = 29
    if ngay >= 1 and ngay <= max :
        print("ngay thang sinh hop le")
        break
    else :
        pass
if (thang == 1 and ngay >= 20) or (thang == 2 and ngay <= 18):
    cung = "Bảo Bình (Aquarius)"
elif (thang == 2 and ngay >= 19) or (thang == 3 and ngay <= 20):
    cung = "Song Ngư (Pisces)"
elif (thang == 3 and ngay >= 21) or (thang == 4 and ngay <= 20):
    cung = "Bạch Dương (Aries)"
elif (thang == 4 and ngay >= 21) or (thang == 5 and ngay <= 20):
    cung = "Kim Ngưu (Taurus)"
elif (thang == 5 and ngay >= 21) or (thang == 6 and ngay <= 21):
    cung = "Song Tử (Gemini)"
elif (thang == 6 and ngay >= 22) or (thang == 7 and ngay <= 22):
    cung = "Cự Giải (Cancer)"
elif (thang == 7 and ngay >= 23) or (thang == 8 and ngay <= 22):
    cung = "Sư Tử (Leo)"
elif (thang == 8 and ngay >= 23) or (thang == 9 and ngay <= 22):
    cung = "Xử Nữ (Virgo)"
elif (thang == 9 and ngay >= 23) or (thang == 10 and ngay <= 23):
    cung = "Thiên Bình (Libra)"
elif (thang == 10 and ngay >= 24) or (thang == 11 and ngay <= 22):
    cung = "Bọ Cạp (Scorpio)"
elif (thang == 11 and ngay >= 23) or (thang == 12 and ngay <= 21):
    cung = "Nhân Mã (Sagittarius)"
else:
    cung = "Ma Kết (Capricorn)"

print(f"Ngày {ngay}/{thang} thuộc cung hoàng đạo: {cung}")

