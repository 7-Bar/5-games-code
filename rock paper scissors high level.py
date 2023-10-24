import random
import os

player_score = 0
computer_score = 0
actual = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Enter your choice: ").lower()
    computer_choice = random.choice(["r", "p", "s"])

    while player_choice not in ["r", "p", "s"]:
        print("Invalid choice")
        player_choice = input("Enter your choice: ").lower()

    player = actual[["r", "p", "s"].index(player_choice)]
    computer = actual[["r", "p", "s"].index(computer_choice)]

    print()
    print(f"you chose {player}, and the computer chose {computer}")
    print()

    if player_choice == computer_choice:
        print("it's a tie!")
    elif player_choice == "r" and computer_choice == "s" or \
         player_choice == "p" and computer_choice == "r" or \
         player_choice == "s" and computer_choice == "p":
        print("you won!")
        player_score += 1
    else:
        print("you lost!")
        computer_score += 1

    print(f"your score: {player_score} | computer score: {computer_score}")
    print()
    input("Press ENTER to continue: ")
    os.system("clear")  # On Mac/Linux
    # os.system("cls")  # On Windows

