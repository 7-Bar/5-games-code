import random
import os

random_number = random.randint(1, 20)
tries = 0

while True:
    tries += 1
    guess = int(input("Enter your guess: "))
    os.system("clear") #on mac/linux
    #os.system("clr") #on windows

    if guess > random_number:
        print(f"{guess} is greater than the number")
    elif guess < random_number:
        print(f"{guess} is smaller than the number")
    else:
        print("you won!")
        break

print(f"you won in {tries} tries")