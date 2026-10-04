import random
player = int(input("How many do you want to loan?: "))
numbers = "12345"
gambling = random.choice(numbers)

entry = int(input("The entry is 100K dollars: "))
if entry <= 100000 and player < 100000:
    print("You don't have enough money")
elif entry >= 100000 and player >= 100000:
    print("You have paid enough money to play")
    player -= 100000
    n = input("Type a number from 1 to 5: ")
    if n != gambling:
        print("You lost 100k Dollars.")
        player -= 100000
        print(f"You have {player} left. ")
    else:
        print("Recieved 1M dollars from MrBeast.")
        player += 1000000
        print(f"You have {player} now.")