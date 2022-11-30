number = int(input())
counter = 1
all_is_printed = False # buleva promenliva

for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(f"{counter}", end = " ") # с end казваш да остане в същия ред
        counter += 1
        if counter > number:
            all_is_printed =True
            break
    if all_is_printed:
        break
    print()

