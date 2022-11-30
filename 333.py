teglo_na_pratkata = float(input())
tip_usloga = input()
raztoqnie_v_kilometri = int(input())
razhod = 0
cena_na_transport = 0
nadcenka_v_kg = 0
nadcenka_v_km = 0
obshta_nadcenka = 0

if tip_usloga == "standard":
    if teglo_na_pratkata <= 1:
        razhod = 3 * raztoqnie_v_kilometri
    elif teglo_na_pratkata <= 10:
        razhod = 5 * raztoqnie_v_kilometri
    elif teglo_na_pratkata <= 40:
        razhod = 10 * raztoqnie_v_kilometri
    elif teglo_na_pratkata <= 90:
        razhod = 15 * raztoqnie_v_kilometri
    elif teglo_na_pratkata <= 150:
        razhod = 20 * raztoqnie_v_kilometri

elif tip_usloga == "express":
    if teglo_na_pratkata <= 1:
        cena_na_transport = raztoqnie_v_kilometri * 3
        nadcenka_v_kg = 3 * 0.8
        nadcenka_v_km = teglo_na_pratkata * nadcenka_v_kg
        obshta_nadcenka = raztoqnie_v_kilometri * nadcenka_v_km
        razhod = cena_na_transport + obshta_nadcenka
    elif teglo_na_pratkata <= 10:
        cena_na_transport = raztoqnie_v_kilometri * 5
        nadcenka_v_kg = 5 * 0.4
        nadcenka_v_km = teglo_na_pratkata * nadcenka_v_kg
        obshta_nadcenka = raztoqnie_v_kilometri * nadcenka_v_km
        razhod = cena_na_transport + obshta_nadcenka
    elif teglo_na_pratkata <= 40:
        cena_na_transport = raztoqnie_v_kilometri * 10
        nadcenka_v_kg = 10 * 0.05
        nadcenka_v_km = teglo_na_pratkata * nadcenka_v_kg
        obshta_nadcenka = raztoqnie_v_kilometri * nadcenka_v_km
        razhod = cena_na_transport + obshta_nadcenka
    elif teglo_na_pratkata <= 90:
        cena_na_transport = raztoqnie_v_kilometri * 15
        nadcenka_v_kg = 15 * 0.02
        nadcenka_v_km = teglo_na_pratkata * nadcenka_v_kg
        obshta_nadcenka = raztoqnie_v_kilometri * nadcenka_v_km
        razhod = cena_na_transport + obshta_nadcenka
    elif teglo_na_pratkata <= 150:
        cena_na_transport = raztoqnie_v_kilometri * 20
        nadcenka_v_kg = 20 * 0.01
        nadcenka_v_km = teglo_na_pratkata * nadcenka_v_kg
        obshta_nadcenka = raztoqnie_v_kilometri * nadcenka_v_km
        razhod = cena_na_transport + obshta_nadcenka

razhod_v_leva = razhod /100
print(f"The delivery of your shipment with weight of {teglo_na_pratkata:.3f} kg. would cost {razhod_v_leva:.2f} lv.")
