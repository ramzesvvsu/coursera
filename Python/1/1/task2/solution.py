import sys
digit_string = sys.argv[1]
sum = 0
for current_len in digit_string:
    sum += int(current_len)
print(sum)