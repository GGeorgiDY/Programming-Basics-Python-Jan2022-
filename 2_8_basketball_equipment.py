annual_tax = int(input())

shoes = annual_tax - (annual_tax * 40 / 100)
equip = shoes - (shoes * 20 / 100)
ball = equip / 4
accesoaries = ball * 0.2

expenses = annual_tax + shoes + equip + ball + accesoaries
print(expenses)
