
#-------------Tim so nguyen to--------------


# def so_nguyen_to():
#     n = int(input("Please type a number: "))
#     if n <= 1:
#             print(f"{n} is not an element number!")
#             return 0
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 print(f"{n} is not an element number!")
#                 return 0
         
#     print(f"{n} is an element number!")

# so_nguyen_to()


#------------Tim so lon nhat-----------------

# List = input("Please type numbers with a period: ")
# List = List.split(",")
# List = [int(x) for x in List]

# Max = List[0]

# for numbers in List:
    
#     if numbers > Max:
#         Max = numbers

# print(f"{Max} is the largest number.")


# a = int(input("Please type your first number: "))
# b = int(input("Please type your second number: "))
# c = int(input("Please type your third number: "))

# Max = a
# if Max < b:
#     Max = b
# if Max < c:
#     Max = c
# print(f"{Max} is the largest number")



a = int(input("Hãy nhập số đầu tiên: "))
b = int(input("Hãy nhập số thứ hai: "))
while a != b:
    if a > b:
        a-=b
    else:
        b-=a

print(f"Ước chung lớn nhất của hai số là: {a}")










# import random
# player = int(input("How many do you want to loan?: "))
# # numbers = "12345"
# gambling = random.choice(numbers)

# entry = int(input("The entry is 100K dollars: "))
# if entry < 100000 and player < 100000:
#     print("You don't have enough money")
# else:
#     print("You have paid enough money to play")
#     player -= 100000
#     n = input("Type a number from 1 to 5: ")
#     if n != gambling:
#         print("You lost 100k Dollars.")
#         player -= 100000
#         print(f"You have {player} left. ")
#     else:
#         print("Recieved 1M dollars from MrBeast.")
#         player += 1000000
#         print(f"You have {player} now.")


