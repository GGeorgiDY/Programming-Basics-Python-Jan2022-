type_flower = input()
amount_flowers = int(input())
budget = int(input())
price = 1

if type_flower == "Roses":
    if amount_flowers > 80:
        price = price * 5.00 * amount_flowers * 0.9
    else:
        price = price * 5.00 * amount_flowers
elif type_flower == "Dahlias":
    if amount_flowers > 90:
        price = price * 3.80 * amount_flowers * 0.85
    else:
        price = price * 3.80 * amount_flowers
elif type_flower == "Tulips":
    if amount_flowers > 80:
        price = price * 2.80 * amount_flowers * 0.85
    else:
        price = price * 2.80 * amount_flowers
elif type_flower == "Narcissus":
    if amount_flowers >= 120:
        price = price * 3.00 * amount_flowers
    else:
        price = price * 3.00 * amount_flowers * 1.15
elif type_flower == "Gladiolus":
    if amount_flowers >= 80:
        price = price * 2.50 * amount_flowers
    else:
        price = price * 2.50 * amount_flowers * 1.20

left_amount = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {amount_flowers} {type_flower} and {left_amount:.2f} leva left.")
else:
    print(f"Not enough money, you need {left_amount:.2f} leva more.")


