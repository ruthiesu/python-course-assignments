import random

secret_number = random.randint(1, 20)

guess = int(input("I'm thinking of a number between 1 and 20. What's your guess? "))

if guess < secret_number:
    print("Too low! The number was", secret_number)
elif guess > secret_number:
    print("Too high! The number was", secret_number)
else:
    print("Correct! You guessed it!")