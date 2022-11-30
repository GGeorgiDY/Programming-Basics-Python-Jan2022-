destination = input()

while destination != "End":
    price_trip = float(input())
    total_saved_money = 0
    while total_saved_money < price_trip:
        saved_money = float(input())
        total_saved_money += saved_money
        if total_saved_money >= price_trip:
            print(f"Going to {destination}!")
            destination = input()


