import random

chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_HOA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
so = "1234567890"
dac_biet = "!@#$%^&*"

password = chu_thuong + chu_HOA + so + dac_biet

length = int(input("Hay nhap do dai: "))
if length < 8:
    print("Too low, Must atleast 8 characters long.")
else:
    print("You can create a password!")

    mk = [random.choice(chu_thuong), random.choice(chu_HOA), random.choice(so), random.choice(dac_biet)]

    for _ in range(length - 4):
        mk.append(random.choice(password))

    random.shuffle(mk)
    matkhau = "".join(mk)
    print("Mat khau:", matkhau)