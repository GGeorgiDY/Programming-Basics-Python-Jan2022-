budget = float(input())
videokart = float(input())
procesiri = float(input())
ram_pamet = float(input())

cena_videokarta = 250
obshto_cena_videokarti = videokart * cena_videokarta

cena_procesor = obshto_cena_videokarti * 0.35
obshto_cena_procesor = procesiri * cena_procesor

cena_ram_pamet = obshto_cena_videokarti * 0.1
obshto_cena_ram_pamet = ram_pamet * cena_ram_pamet

kraina_smetka = obshto_cena_videokarti + obshto_cena_procesor + obshto_cena_ram_pamet

if videokart > procesiri:
    kraina_smetka *= 0.85

difference = abs(budget - kraina_smetka)

if budget > kraina_smetka:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
