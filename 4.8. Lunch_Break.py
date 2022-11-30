import math

ime_na_serial = str(input())
prodaljitelnost_na_epizod = float(input())
prodaljitelnost_na_pochivka = float(input())

vreme_za_obqd = prodaljitelnost_na_pochivka * 0.125
vreme_za_otdih = prodaljitelnost_na_pochivka * 0.25
svobodno_vreme_za_flim = prodaljitelnost_na_pochivka - vreme_za_obqd - vreme_za_otdih
difference = abs(math.ceil(prodaljitelnost_na_epizod - svobodno_vreme_za_flim))

if prodaljitelnost_na_epizod <= svobodno_vreme_za_flim:
    print(f"You have enough time to watch {ime_na_serial} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {ime_na_serial}, you need {difference} more minutes.")
