#suma = depozirana suma + srok na depozita *((depozina suma*godishen procent)/12)
deposit = float(input())
months = int(input())
annual_interest_percent = float(input())

annual_interest = deposit * annual_interest_percent / 100
monthly_interest = annual_interest / 12
total_sum = deposit + months * monthly_interest
print(total_sum)

#suma = deposit + months * ((deposit*annual_interest_percent)/12)

