import sys
num_steps = int(sys.argv[1])
count = int(num_steps)
for i in range(1, count+1):
    print(" "*(count-i) + "#"*i)