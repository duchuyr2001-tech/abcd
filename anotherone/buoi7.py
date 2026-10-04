import random

chu_thuong = "abcdefghijklmnopqrstuvwxyz"
chu_HOA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
so = "1234567890"
dac_biet = "!@#$%^&*"

password = chu_thuong + chu_HOA + so + dac_biet

length = int(input("Hay nhap do dai: "))
if length < 8:
    print("Too low, Must atleast 8 characters long")
else:
    print("You can create a password!")

    mk = [random.choice(chu_thuong), random.choice(chu_HOA), random.choice(so), random.choice(dac_biet)]

    for _ in range(length - 4):
        mk.append(random.choice(password))

    random.shuffle(mk)
    matkhau = "".join(mk)
    print("Mat khau:", matkhau)


#----------------------------- BAI TAP ----------------------------------------




# import random
# xuc_xac = "123456"
# dice = ["Head", "Tails"]
# rand = random.choice(xuc_xac)
# ran = random.choice(dice)
# print("Ban da tung duoc:", rand)
# print("Ban da tung duoc:", ran)

# import random

# OTP_code = ("OTP:", random.randint(100000,999999))
# print(OTP_code)

# import random

# ten = ["Lan", "An", "Binh", "Cuong"]
# random.shuffle(ten)
# print(ten)

# import random

# chu_inthuong = "abcdefghijklmnopqrstivwxyz"
# word = random.choice(chu_inthuong)
# print(word)

# list = ["P","y","t","h","o","n"]
# ky_tu = "".join(list)
# print(ky_tu)

# import random

# list = []
# for _ in range(5):
#     list.append(random.randint(0, 9))

# print(list)