# num = int(input("Hay nhap so: "))
# for i in range(1,num):
#     print(i)

# n = int(input("Nhap mot so: "))
# def tat_ca_cac_so():
#     for i in range(1,n,1):
#         print(i)
# def so_chan():
#     for i in range(1,n,1):
#         if i % 2 == 0:
#             print(i)

# def so_le():
#     for i in range(1,n,1):
#         if i % 2 != 0:
#             print(i)

# def tong_cac_so():
#     tong = 0
#     for i in range(1,n,1):
#         tong += i
#         print("Tong cac so tu 1 den ",n,"la",tong)
# def bang_cuu_chuong():
#     for i in range(1,11,1):
#         print(n,"x",i,"=",n*i)


# num = int(input("Hay nhap so: "))
# for i in range(num,0,-1):
#     print(i)


# a = int(input("Nhap so thu nhat"))
# b = int(input("Nhap so thu nhat"))
# c = int(input("Nhap so thu nhat"))

# max = a

# if b > max:
#    max = b
# elif c > max:
#    max = c

# print("So lon nhat la", max)

a = int(input("Nhap mot so: "))
daonguoc = 0
while a > 0:
    daonguoc = daonguoc*10+a%10
    a = a//10
print(daonguoc)



