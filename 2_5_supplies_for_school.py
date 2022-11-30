number_of_pens = int(input())
numbers_of_markers = int(input())
litres_of_detergent = int(input())
percent_discount = int(input())

price_per_pens = 5.80
price_per_markers = 7.20
price_per_liter_detergent = 1.20

needed_sum = number_of_pens * price_per_pens + \
             numbers_of_markers * price_per_markers + \
             litres_of_detergent * price_per_liter_detergent
needed_sum = needed_sum - needed_sum * percent_discount / 100
#gorniq red moje da se napishe i taka => needed_sum -= needed_sum * percent_discount / 100
print(needed_sum)

