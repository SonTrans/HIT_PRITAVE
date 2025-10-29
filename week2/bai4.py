email = input("nhap email : ")
if "@" in email and "." in email:
    for i in range(len(email)):
        if email[i] == "@" :
            acong = i
        if email[i] == "." :
            cham = i
            break
    if 0 < acong < cham +1 < len(email) :
        print("email hop le")
    else :
        print("email khong hop le")
else:
    print("email khong hop le")