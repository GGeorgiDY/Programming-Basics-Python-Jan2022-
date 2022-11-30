import math
percent_fat = int(input())
percent_protein = int(input())
percent_vyglehidrat = int(input())
total_calories = int(input())
percent_voda = int(input())

gram_maznini = 9
gram_protein = 4
gram_vyglehidrat = 4

obshti_gramove_maznini = ((percent_fat / 100) * total_calories) / gram_maznini
obshti_gramove_protein = ((percent_protein / 100) * total_calories) / gram_protein
obshti_gramove_vyglehidrati = ((percent_vyglehidrat / 100) * total_calories) / gram_vyglehidrat

teglo_na_hrana = obshti_gramove_maznini + obshti_gramove_protein + obshti_gramove_vyglehidrati
kalorii_per_den = total_calories / teglo_na_hrana
kalorii_per_den_bez_voda = kalorii_per_den - (kalorii_per_den * percent_voda / 100)
print(f"{kalorii_per_den_bez_voda:.4f}")

