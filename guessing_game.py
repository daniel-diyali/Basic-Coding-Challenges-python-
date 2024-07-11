# The following program does a guessing game
import random

number = random.randint(1, 5)
answer = int(number)
guessed = False
count = 1
while not guessed:
    ask = input("Guess a number: ")
    guess = int(ask)
    if guess == answer:
        print("You got it! It took you " + str(count) + " tries.")
        guessed = True
    elif guess > answer:
        print("Wrong, lower")
        count += 1
    elif guess < answer:
        print("Wrong, higher")
        count += 1
    else:
        print("Wrong. Try again")
        count += 1

