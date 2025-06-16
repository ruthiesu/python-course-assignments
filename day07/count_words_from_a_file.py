import sys
if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

try:
    with open(filename, "r") as input_file:
        input_text = input_file.read()
except Exception as err:
    print('Could not read file:', filename, err)
    exit(1)

input_text = input_text.lower()  # I see in the example you considered Ut and ut as the same word

words = input_text.split()
my_map = {}

for obj in words:
    if obj in my_map:
        my_map[obj] += 1
    else:
        my_map[obj] = 1

for key, value in my_map.items():
    print(f"{key:<14}  {value:>3}")