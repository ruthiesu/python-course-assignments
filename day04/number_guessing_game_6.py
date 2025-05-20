import random

secret_num = random.randrange(1, 21)
game_over = False
debug_mode = False
move_mode = False
while not game_over:
    if debug_mode:
        print("Debug mode: secret number is " + str(secret_num))
    guess = input("Guess the number (1-21): ")
    if move_mode:
        secret_num += random.randrange(-2, 3)
    if guess == 'x':
        game_over=True
    elif guess == 's':
        print("Secret number is: " + str(secret_num) + " now you try")
    elif guess == 'd':
        debug_mode = not debug_mode
    elif guess == 'n':
        print("------------- New game --------------13")
        secret_num = random.randrange(1, 21)
    elif guess.isnumeric():
        if int(guess) < secret_num:
            print("Too low!")
        elif int(guess) > secret_num:
            print("Too high!")
        else:
            print("Correct!")
            game_over=True
    if guess == 'm':
        move_mode = not move_mode
        if move_mode:
            print("move mode on")
        else:
            print("move mode off")
print("bye")
