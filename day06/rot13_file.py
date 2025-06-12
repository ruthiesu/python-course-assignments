# Implement ROT13:
# Create a script called rot13_file.py that given a file on the command line it will replace the content with the rot13 of it of it.

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

result = ""
for c in input_text:
    if c.isalpha():
        if c.islower():
            result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    else:
        result += c
try:
    with open(filename, 'w') as output_file:
        output_file.write(result)

except Exception as err:
    print('Could not write file:', filename, err)
    exit(1)
