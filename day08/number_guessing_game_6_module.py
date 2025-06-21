import random

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
