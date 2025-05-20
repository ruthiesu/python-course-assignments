import random

secret_num = random.randrange(1, 21)
print(secret_num)
game_over = False

while not game_over:
    guess = input("Guess the number (1-21): ")
    if guess == 'x':
        game_over=True
    elif guess.isnumeric():
        if int(guess) < secret_num:
            print("Too low!")
        elif int(guess) > secret_num:
            print("Too high!")
        else:
            print("Correct!")
            game_over=True
print("bye")

