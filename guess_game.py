import random

number = random.randint(1, 10)

print("Welcome to Number Guessing Game!")

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess!")
    print("The correct number was:", number)
