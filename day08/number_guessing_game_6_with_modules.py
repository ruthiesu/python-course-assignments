import random
from number_guessing_game_6_module import *

secret_num = generate_secret_num()
game_over = False
debug_mode = False
move_mode = False
while not game_over:
    if debug_mode:
        print_debug_info(secret_num)
    guess = input("Guess the number (1-21): ")
    if move_mode:
        secret_num += random.randrange(-2, 3)
    if guess == 'x':
        game_over=True
    elif guess == 's':
        print("Secret number is: " + str(secret_num) + " now you try")
    elif guess == 'd':
        debug_mode = toggle_mode("debug", debug_mode)
    elif guess == 'n':
        print("------------- New game --------------")
        secret_num = generate_secret_num()
    elif guess.isnumeric():
        game_over = evaluate_guess(guess, secret_num)
    elif guess == 'm':
        move_mode = toggle_mode("move", move_mode)
    else:
        print("Invalid input, try again.")
print("bye")
