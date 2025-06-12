import re
import sys
if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

try:
    with open(filename, "r") as input_file:
        digits = input_file.read()
except Exception as err:
    print('Could not read file:', filename, err)
    exit(1)


digits = re.sub(r'\s+', '', digits)
counters = [0]*10

for d in digits:
    counters[int(d)]+=1

for i in range(len(counters)):
    print(f"{i:>5}  {counters[i]:>5}")