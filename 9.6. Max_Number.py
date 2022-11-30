import sys
n = input()
max_num = -sys.maxsize

while n != "Stop":
    current_number = int(n)
    if current_number > max_num:
        max_num = current_number
    n = input()
print(max_num)
