ctr_sea = int(input())
ctr_mountain = int(input())

ctr_sea_sales = 0
ctr_mountain_sales = 0
sales_amount = 0
while (ctr_sea > ctr_sea_sales) | (ctr_mountain > ctr_mountain_sales):
    command = str(input())
    if command == "Stop":
        break
    elif command == "sea":
        ctr_sea_sales += 1
        if ctr_sea_sales <= ctr_sea:
            sales_amount += 680
    else:
        ctr_mountain_sales += 1
        if ctr_mountain_sales <= ctr_mountain:
            sales_amount += 499

if (ctr_sea_sales >= ctr_sea) & (ctr_mountain_sales >= ctr_mountain):
    print("Good job! Everything is sold.")

print(f"Profit: {sales_amount:.0f} leva.")
