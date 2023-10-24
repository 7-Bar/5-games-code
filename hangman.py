import random

tries = 0
words = ["truck", "car", "computer", "ice", "cream"]
guess_list = []
word = random.choice(words)

for x in range(len(word)):
    guess_list.append("_")

while guess_list.__contains__("_"):
    for x in range(len(guess_list)):
        print(guess_list[x], end = " ")

    print()

    guess = input("Enter your guess: ")

    while len(guess) != 1:
        print("invalid choice")
        guess = input("Enter your guess: ")
    
    if word.__contains__(guess):
        guess_list[word.index(guess)] = guess
    
    tries += 1

print(f"you won in {tries} tries!")