chuoi = input("Nhap chuoi : ").lower()
list1 =[]
for i in chuoi:
    if i.isalnum():
        if i.isdigit():
            continue
        list1.append(i)
dic = {}
for i in list(list1):
    dic[i] = list(list1).count(i)
print(dic)
