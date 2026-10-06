import random

print("WELCOME TO DICE ROLLING GAME")

while True :

    choice = input("\nEnter 1 to roll the dice or 0 to stop: ")

    if choice == "1":
        roll = random.randint(1, 6)
        print("You rolled:", roll)

    elif choice == "0":
        print(" Game stopped. Thanks for playing! ")
        break

    else:
        print("Invalid input! Please enter only 1 or 0.")