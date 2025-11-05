import math
numbers = [2, 3, 2, -4, 3, 5]
numbers_1 = set(numbers)
numbers_2=[]
for i in list(numbers_1):
    if abs(i) % 2 == 0:
        i = i * i
        numbers_2.append(i)
    else :
        i = i * i * i
        numbers_2.append(i)
tong = 0
demso = 0
for x in range(len(numbers)):
    if x % 2 == 0:
        tong = tong + list(numbers)[x]
        demso += 1
numbers_3 = list(numbers_1).copy()
for y in range(len(numbers_3) - 1):
    for j  in range(y+1,len(numbers_3) ):
        if abs(numbers_3[y]) > abs(numbers_3[j]):
            a = numbers_3[j]
            numbers_3[j] = numbers_3[y]
            numbers_3[y] = a
        else :
            continue
print(f"Sau khi loại trùng :{list(numbers_1)}")
print(f"List mới : {numbers_2}")
print(f"TBC các phần tử ở vị trí trong list ban đầu là: {tong/demso}")
print(f"Sắp xếp tăng dần theo abs : {numbers_3}")
