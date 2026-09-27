import random
password_length = int(input("How long is your password? (Atleast 9 characters long): "))

chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_hoa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
so = "0123456789"
dac_biet = "!@#$%^&*"

storage = chu_hoa + chu_thuong + so + dac_biet

mat_khau = ""

for i in range(password_length):
    ky_tu = random.choice(storage)
    mat_khau = mat_khau + ky_tu

print(mat_khau)
