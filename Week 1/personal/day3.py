# Guessing Game
import random

randomNum = random.randint(1,11)
# print(randomNum) # To know what is your random number generate by computer.

for i in range(5):
    guessNum = int(input("Enter your guess number between 1 to 5 here: "))
    if guessNum > 5:
        print("*" * 10)
        print("Guess a number between 1 to 5.")
        print("*" * 10)
    elif guessNum == randomNum:
        print('*' * 50)
        print(f"You got the correct guess number in {i+1} tries .")
        print("*" * 50)
        break;
    elif guessNum > randomNum:
        print("*" * 50)
        print("Your guess number is greater than random number")
        print("*" * 50)
    elif guessNum < randomNum:
        print("*" * 50)
        print("Your guess number is less than random number")
        print("*" * 50)
    if i == 4:
        print("*" * 50)
        print("Your are a bad guesser!")
        print("*" * 50)
