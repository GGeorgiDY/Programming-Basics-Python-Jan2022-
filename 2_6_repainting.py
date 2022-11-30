#needed_nailon_per_sqrt_meter = int(input())
#needed_paint_per_litre = int(input())
#needed_paint_razreditel_per_litre = int(input())
#needed_working_hours = int(input())

#price_nailon_per_sqrt_meter = 1.50
#price_paint_per_litre = 14.50
#price_paint_razreditel_per_liter = 5.00

#additional_paint_per_litre = paint_per_litre * 0.10
#additional_nailon_per_sqrt_meter = 2
#additional_bags = 0.4

#total_amount_nailon = (needed_nailon_per_sqrt_meter + additional_nailon_per_sqrt_meter) * price_nailon_per_sqrt_meter
#total_amount_paint = (needed_paint_per_litre + additional_paint_per_litre) * price_paint_per_litre
#total_amount_razreditel = needed_paint_razreditel_per_litre +

#workers_salary =

nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

materials_sum = (nylon + 2) * 1.50 + \
                (paint * 1.1) * 14.50 + \
                (thinner * 5) + \
                (0.4)
salary = materials_sum * 0.3 * hours
total_sum = materials_sum + salary
print(total_sum)
