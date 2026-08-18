diemtoan = int(input("Hay nhap diem toan: "))
diemvan = int(input("Hay nhap diem van: "))
diemhoa = int(input("Hay nhap diem hoa: "))
trungbinh = (diemhoa + diemvan + diemtoan)
if trungbinh >= 8:
    print("Hoc sinh gioi")
elif trungbinh >= 5:
    print("Hoc Sinh Kha")
elif trungbinh >= 3:
    print("Hoc Sinh Trung Binh")
else:
    print("Hoc Sinh Yeu")