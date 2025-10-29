n = int(input("nhap so nguyen n :"))
giaithua1 = 1
S =0
for i in range(1,n+1):
    giaithua1 = giaithua1*i
    S = S + 1/giaithua1
print(f"S = {S} ")
x = float(input("nhap so thuc x :"))
sum = 1 + x
giaithua2 = 1
for j in range(2,n+1):
    giaithua2 = giaithua2*j
    sum = sum + pow(x,j)/giaithua2
print(f"e^{x} = {sum}")