djobni = float(input())
pechalba_na_den_ot_prodajbi = float(input())
razhodi_za_celiq_period = float(input())
cena_na_podarak = float(input())

spesteni_pari_ot_djobni = djobni * 5
specheleni_pari = pechalba_na_den_ot_prodajbi * 5
obshto_spesteni_pari = spesteni_pari_ot_djobni + specheleni_pari
spesteni_pari_minus_razhodite = obshto_spesteni_pari - razhodi_za_celiq_period

difference = abs(spesteni_pari_minus_razhodite - cena_na_podarak)
if spesteni_pari_minus_razhodite >= cena_na_podarak:
    print(f"Profit: {spesteni_pari_minus_razhodite:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {difference:.2f} BGN.")