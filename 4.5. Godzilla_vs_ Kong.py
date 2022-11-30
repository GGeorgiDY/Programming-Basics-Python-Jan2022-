budget = float(input())
statisti = int(input())
cena_za_obleklo_na_statist = float(input())

decor = budget * 0.1
cena_na_vsichki_drehi = statisti * cena_za_obleklo_na_statist
if statisti > 150:
    cena_na_vsichki_drehi *= 0.9
nujni_pari = decor + cena_na_vsichki_drehi
difference = abs(nujni_pari - budget)
if nujni_pari > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")

