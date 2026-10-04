# def cong():
#     print(a+b)

# def tru():
#     print(a-b)

# def nhan():
#     print(a*b)

# def chia():
#     print(a/b)

# while True:
#     a = int(input("Nhap so thu nhat: "))
#     b = int(input("Nhap so thu hai: "))
#     c = int(input("Chon mode: "))
#     if c == 1:
#         cong()

#     if c == 2:
#         tru()

#     if c == 3:
#         nhan()

#     if c == 4:
#         chia()
#     else:
#         cong()
#         tru()
#         nhan()
#         chia()


# def so_chan():
#     for i in range(1,n,1):
#         if i % 2 == 0:
#             print(i,"la so chan")
# def so_le():
#     for i in range(1,n,1):
#         if i % 2 != 0:
#             print(i, "la so le")

# while True:        
#     n = int(input("Hay nhap so: "))
#     m = int(input("Hay chon mode: "))
#     if m == 1:
#         so_chan()
#     elif m == 2:
#         so_le()
#     else:
#         so_chan()
#         so_le()

# def nam_nhuan():
#     if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
#         print(n,"la nam nhuan")
#     else:
#         print("khong phai la nam nhuan")
# n = int(input("Hay nhap nam: "))
# nam_nhuan()

def cong():
    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))
    print("Ket qua: ", a + b)
def tru():
    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))
    print("Ket qua: ", a - b)
def nhan():
    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))
    print("Ket qua: ", a * b)
def chia():
    a = int(input("Nhap so thu 1: "))
    b = int(input("Nhap so thu 2: "))
    print("Ket qua", a/b, "\nKet qua: ", a % b, "\nKet qua: ", a // b)
def binhphuong():
    a = int(input("Nhap so thu 1: "))
    print("Ket qua: ", a * a)

while True:
    print("="*30)
    print("1. Phep cong \n2. Phep tru \n3. Phep nhan \n4.Phep chia: \n-Chia lay du \n-Chia lay nguyen \n5. Binh Phuong \n0. Thoat")
    mode = int(input("Hay chon 1 so: "))
    if mode == 1:
        cong()
    elif mode == 2:
        tru()
    elif mode == 3:
        nhan()
    elif mode == 4:
        chia()
    elif mode == 5:
        binhphuong()
    elif mode == 0:
        break
    else:
        print("Please choose the corret number")


