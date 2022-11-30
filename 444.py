pc_number = int(input())

total_sales = 0
total_rating = 0

for i in range(1, pc_number + 1):
    item_number = str(input())
    item_rating = item_number[-1:] #взимаш последната цифра
    item_sales = item_number[:2] #взимаш  първите две цифри

    if item_rating == "2":
        multiplier = 0
    elif item_rating == "3":
        multiplier = 0.5
    elif item_rating == "4":
        multiplier = 0.7
    elif item_rating == "5":
        multiplier = 0.85
    else:
        multiplier = 1.00

    total_rating += int(item_rating)
    total_sales += int(item_sales) * multiplier

print(f"{total_sales:.2f}")
print(f"{(total_rating / pc_number):.2f}")


print(f"{total_sales:.2f}")
print(f"{}")