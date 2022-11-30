budget = float(input())
season = input()
place = "Camp"
destination = "asd"
price = 0

if budget <= 100:
    destination = "Bulgaria"
    print("Somewhere in Bulgaria")
    if season == "summer":
        price = budget * 0.3
        place = "Camp"
        print(f"{place} - {price:.2f}")

    else:
        price = budget * 0.7
        place = "Hotel"
        print(f"{place} - {price:.2f}")

elif budget <= 1000:
    print("Somewhere in Balkans")
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        place = "Camp"
        print(f"{place} - {price:.2f}")
    else:
        price = budget * 0.8
        place = "Hotel"
        print(f"{place} - {price:.2f}")
else:
    destination = "Europe"
    print("Somewhere in Europe")
    price = budget * 0.9
    place = "Hotel"
    print(f"{place} - {price:.2f}")





