projections = str(input())
redove = int(input())
coloni = int(input())
price = 0

if projections == "Premiere":
    price = 12 * redove * coloni
elif projections == "Normal":
    price = 7.50 * redove * coloni
elif projections == "Discount":
    price = 5 * redove * coloni

print(f"{price:.2f} leva")

