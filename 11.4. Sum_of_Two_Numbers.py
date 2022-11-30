beggining_interval = int(input())
ending_interval = int(input())
magic_number = int(input())
all_combinations = 0
combination_number = 0
flag = False

for i in range(beggining_interval, ending_interval + 1):
    for j in range(beggining_interval, ending_interval + 1):
        all_combinations += 1
        sum = i + j
        if sum == magic_number:
            print(f"Combination N:{all_combinations} ({i} + {j} = {magic_number})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{all_combinations} combinations - neither equals {magic_number}")