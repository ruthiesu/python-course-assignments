import random

secret_num = random.randrange(1, 21)
print(secret_num)
guess = int(input("Guess the number (1-21): "))
if guess < secret_num:
    print("Too low!")
elif guess > secret_num:
    print("Too high!")
else:
    print("Correct!")

