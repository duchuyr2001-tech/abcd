# ten = input("Nhap ten ban: ").strip().title()
# color = input("Nhap mau yeu thich: ").strip().title()
# animal = input("Nhap con vat yeu thich: ").strip().title()

# biet_danh = f"{color} {animal} Huyen Thoai"
# print(f"{ten}. biet danh sieu anh hung cua ban la: {biet_danh}!")

#.strip().title(): lam sach string va in hoa chu cai dau

#---------- Bai 1,2,3-------------

# var = input("Hay nhap chu vao: ")
# print(var.upper())

# var2 = input("Hay dien chu vao: ")
# print(len(var2))

# var3 = input("Hay dien tu vao: ")
# print("Dau: ",var3[0], "\nCuoi: ",var3[-1])

# ---------Bai 4,5,6,7,8------------

# var4 = input("Hay dien tu vao: ")
# print(var4[::-1])

# var5 = input("Hay nhap tu vao: ")
# print(var5[0:3])

# ten = input("Hay nhap ten cua ban: ")
# tuoi = int(input("Hay nhap tuoi cua ban: "))
# print(f"Minh ten la {ten}, nam nay minh {tuoi} tuoi.")

# var7 = input("Hãy nhập tên của bạn: ")
# print(var7.strip().title())

# var8 = input("Hay nhập một ký tự: ")
# print(var8*10)

#--------Bài 9------------
First_name = input("Enter your first name: ").strip().title()
Last_name = input("Enter your last name: ").strip().title()
print(f"{First_name[0].upper()}.{Last_name[0].upper()}")