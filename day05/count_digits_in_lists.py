numbers = [1203, 1256, 312456, 98]
digits = ''
for n in numbers:
       digits += str(n)

counters = [0]*10

for d in digits:
    counters[int(d)]+=1

for i in range(len(counters)):
    print(f"{i:>5}  {counters[i]:>5}")