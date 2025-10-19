a= int(input("Nhập số a = "))
b= int(input("Nhập số b = "))
print(f"{a}+{b} = {a+b}")
print(f"{a}-{b} = {a-b}")
print(f"{a}*{b} = {a*b}")
print(f"{a}:{b} = {a//b}")
print(f"{a} mũ {b} = {a**b}")
print(f"{a}:{b} = {a//b} dư {a%b}")
if (a>b):
    print(f"{a} > {b}")
elif (b>a):
    print(f"{b} > {a}")
else :
    print(f"{a} = {b}")
print(bool(a and b)) # trả về a nếu a = 0, =b trong mọi TH khác
print(bool(a or b))    # ngược lại với and
print(bool(a ^ b))     # a = b thì trả về false và true trông mọi TH khác
print(not (a == b))    
print(f"{a} dịch phải 5 bit = {a >> 5}")
print(f"{a} dịch trái 6 bit = {a << 6}")
bit = bin(a)[2:]
kq = bit[::-1]
print(f"hệ cơ số 2 đảo ngược của {a} là {~bit}")