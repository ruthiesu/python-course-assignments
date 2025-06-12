# Create a file similar to the colors.txt file and use it as the list of colors in the earlier example where we prompted for a color.
# Call the new script color_selector_file.py

#
# In a script called color_selector_menu.py have a list of colors. Write a script that will display a menu (a list of numbers and the corresponding color) and prompts the user for a number. The user needs to type in one of the numbers. That's the selected color.
# blue
# green
# yellow
# white
# For extra credit make sure the system is user-proof and it won't blow up on various incorrect input values. (e.g Floating point number. Number that is out of range, non-number)
# For more credit allow the user to supply the number of the color on the command line. python color_selector_menu.py 3. If that is available, don't prompt.
# For further credit allow the user to provide the name of the color on the command line: python color_selector_menu.py yellow Can you handle color names that are not in the expected case (e.g. YelloW)?
# Any more ideas for improvement?


import sys
if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

try:
    with open(filename, "r") as input_file:
        lines = input_file.readlines()
except Exception as err:
    print('Could not read file:', filename, err)
    exit(1)

for i in range(len(lines)):
    lines[i].strip()

done = False
while not done:
    print("Available colors:")
    for i in range(len(lines)):
        print(f"{i+1}: {lines[i].strip()}")
    choice = input("Please select a color by number: ")
    try:
        choice = int(choice)
        if 1 <= choice <= len(lines):
            print(f"You chose: {lines[choice-1].strip()}")
            done = True
        else:
            print("Invalid choice. Please select a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")