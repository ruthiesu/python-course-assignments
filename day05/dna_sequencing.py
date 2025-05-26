import re
import sys

seq = sys.argv[1]
print("before: "+ seq)

seq_list = re.split(r'X+', seq) # split on 'X'

seq_list.sort(key=len)
seq_list[:] =[s for s in seq_list if s] # remove empty strings

print("after: " + str(seq_list))
