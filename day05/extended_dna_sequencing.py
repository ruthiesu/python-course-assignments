import re
import sys
seq = input("Please type in a sequence:")
print("before: "+ seq)

seq_list = re.split(r'[^ACGT]+', seq) # split on 'X'

seq_list.sort(key=len)
seq_list[:] =[s for s in seq_list if s] # remove empty strings

print("after: " + str(seq_list))
