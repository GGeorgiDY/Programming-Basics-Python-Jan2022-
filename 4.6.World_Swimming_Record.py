rekord_v_sekundi = float(input())
raztoqnie_v_metri = float(input())
vremeto_v_sekundi_za_1_metar = float(input())

vreme_za_da_prepluva_cqloto_raztoqnie = raztoqnie_v_metri * vremeto_v_sekundi_za_1_metar
pyti_zabavqne = raztoqnie_v_metri // 15
vreme_zabavqne = pyti_zabavqne * 12.5
cqlostno_vreme_za_prepluvane = vreme_za_da_prepluva_cqloto_raztoqnie + vreme_zabavqne
razlika = abs(rekord_v_sekundi - cqlostno_vreme_za_prepluvane)

if rekord_v_sekundi > cqlostno_vreme_za_prepluvane:
    print(f" Yes, he succeeded! The new world record is {cqlostno_vreme_za_prepluvane:.2f} seconds.")
else:
    print(f"No, he failed! He was {razlika:.2f} seconds slower.")
