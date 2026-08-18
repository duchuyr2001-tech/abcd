# def line():
#     print("==========================================")
# def cong():
#     print("Phep Cong")
#     a = float(input("Nhap so thu 1: "))
#     b = float(input("Nhao si thu 2: "))
#     print("Ket qua: ", a + b)
# def tru():
#     print("Phep tru")
#     a = float(input("Nhap so thu 1: "))
#     b = float(input("Nhao si thu 2: "))
#     print("Ket qua: ", a - b)
# def nhan():
#     print("Phep nhan")
#     a = float(input("Nhap so thu 1: "))
#     b = float(input("Nhao si thu 2: "))
#     print("Ket qua: ", a * b)
# def chia():
#     print("Phep chia")
#     a = float(input("Nhap so thu 1: "))
#     b = float(input("Nhao si thu 2: "))
#     if b == 0:
#         print("Ko the chia cho 0")
#     else:
#         print("Ket qua: ", a / b)
# def phan_nguyen():
#     print("Lay Phan Nguyen")
#     a = float(input("Nhap so thu 1: "))
#     b = float(input("Nhao si thu 2: "))
#     if b == 0:
#         print("Ko the chia cho 0")
#     else:
#         print("Ket qua: ", a // b)
# def phan_du():
#     print("Lay Phan Du")
#     a = float(input("Nhap so thu 1: "))
#     b = float(input("Nhao si thu 2: "))
#     if b == 0:
#         print("Ko the chia cho ko")
#     else:
#         print("Ket qua: ", a % b)
# def binh_phuong():
#     print("Binh Phuong")
#     a = float(input("Hay nhap so: "))
#     print("Key qua: ", a * a)
# while True:

#     print("Menu May Tinh")
#     print("1. Phep cong")
#     print("2. Phep tru")
#     print("3. Phep nhan")
#     print("4. Phep chia")
#     print("5. Chia Lay Phan Nguyen")
#     print("6. Chia lay phan du")
#     print("7. Binh Phuong")
#     print("0. Thoat")
#     line()
#     decision = int(input("Nhap lua chon: "))
#     if decision == 1:
#         cong()
#     elif decision == 2:
#         tru()
#     elif decision == 3:
#         nhan()
#     elif decision == 4:
#         chia()
#     elif decision == 5:
#         phan_nguyen()
#     elif decision == 6:
#         phan_du()
#     elif decision == 7:
#         binh_phuong()
#     elif decision == 0:
#         break
#     else:
#         print("Hay chon mode lai ")

taikhoan = ""
matkhau = ""
def line():
    print("==============================")
def dang_ki():
    global taikhoan, matkhau
    if taikhoan != "":
        print("Tai khoan da dc dang ki")
    else:
        taikhoan = input("Hay nhap ten: ")
        matkhau = input("Hay nhap mat khau: ")
        print("Dang ki thanh cong")
    
def dang_nhap():
    ten = input("Hay nhap ten dang nhap: ")
    mk = input("Hay nhap mat khau dang nhap: ")
    if ten == taikhoan:
        if mk == matkhau:
            print("Dang nhap thanh cong")
        else:
            print("Sai mat khau")
    else:
        print("Sai ten")
def quen_mat_khau():
    global matkhau
    ten = input("Hay nhap ten dang nhap: ")
    if ten == taikhoan:
        mk_moi = input("Hay nhap mat khau moi: ")
        print("Doi mat khau thanh cong")
        matkhau = mk_moi
    else:
        print("Tai khoan ko ton tai")
def doi_mat_khau():
    mk = input("Hay nhap mat khau cu")
    if matkhau == mk:
        mk_moi = input("Hay nhap mat khau moi")
    else:
        print("Mat khau cu ko dung")
def thoat():
    print("Tam biet")
while True:
    print("1. Dang Ki")
    print("2. Dang Nhap")
    print("3. Quen Mat Khau")
    print("4. Doi Mat Khau")
    print("5. Thoat")
    line()
    luachon = int(input("Nhap so lua chon: "))
    if luachon == 1:
        dang_ki()
        print("===================")
    elif luachon == 2:
        dang_nhap()
        print("===================")
    elif luachon == 3:
        quen_mat_khau()
        print("===================")
    elif luachon == 4:
        doi_mat_khau()
        print("===================")
    elif luachon == 5:
        thoat()
        print("===================")
        break
    

    

    