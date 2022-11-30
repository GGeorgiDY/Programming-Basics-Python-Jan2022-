number = int(input())
bonus_tochki = 0
if number <= 100:
    bonus_tochki += 5
elif number <= 1000:
    bonus_tochki += number * 0.2
else:
    bonus_tochki += number * 0.1
if number % 2 == 0:
    bonus_tochki += 1
if number % 10 == 5:
    bonus_tochki += 2
print(bonus_tochki)
print(bonus_tochki+number)


