pileshko = int(input())
riba = int(input())
vegetariansko = int(input())

cena_pileshko = pileshko * 10.35
cena_riba = riba * 12.40
cena_vegetariansko = vegetariansko * 8.15
cena_desert = (cena_pileshko + cena_riba + cena_vegetariansko) * 0.2
dostavka = 2.5
suma = cena_pileshko + cena_riba + cena_vegetariansko + cena_desert + dostavka
print(suma)


