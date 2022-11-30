daljina = int(input())
shirochina = int(input())
visochina = int(input())
percent_zaetost = int(input())

#obem na akvariuma = lenght *shorochina *hight
obem = daljina * shirochina * visochina
obem_v_litri = obem / 1000
zaeto_prostranstvo_v_procent = percent_zaetost / 100
needed_litres = obem_v_litri - (obem_v_litri * zaeto_prostranstvo_v_procent)
print(needed_litres)
