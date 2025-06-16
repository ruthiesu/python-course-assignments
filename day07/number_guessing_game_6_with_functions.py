import random

# I didn't define any variables in the functions even though you specifically ased, becasue none of the functions needed local variables, they were all modes of the game. i did pass them as parameters, for what it's worth in such a simple game.


def generate_secret_num(): #this will help if i want to change the range in one place
    return random.randrange(1, 21)

def print_debug_info(secret_number): #this will help if i want to add more stats etc (not meant to refactor away output handling).
    print(f"Debug mode: secret number is {secret_number}")

def toggle_mode(name, current_value):
    new_value = not current_value
    print(f"{name} mode {'on' if new_value else 'off'}")
    return new_value

def evaluate_guess(guess, secret_number):
    guess = int(guess)
    if guess < secret_number:
        print("Too low!")
        return False
    elif guess > secret_number:
        print("Too high!")
        return False
    else:
        print("Correct!")
        return True

# generally i would refactor away the input and output handling, but this is such a small exercise it may be over-complicating

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
    if guess == 'm':
        move_mode = toggle_mode("move", move_mode)

print("bye")
