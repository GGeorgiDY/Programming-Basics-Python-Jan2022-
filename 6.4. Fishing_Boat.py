budget = int(input())
season = input()
fisherman = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent += 3000
    if fisherman <= 6:
        boat_rent = boat_rent * 0.9
    elif fisherman <= 11:
        boat_rent = boat_rent * 0.85
    elif fisherman > 11:
        boat_rent = boat_rent * 0.75

elif season == "Winter":
    boat_rent += 2600
    if fisherman <= 6:
        boat_rent = boat_rent * 0.9
    elif fisherman <= 11:
        boat_rent = boat_rent * 0.85
    elif fisherman > 11:
        boat_rent = boat_rent * 0.75

elif season == "Summer" or season == "Autumn":
    boat_rent += 4200
    if fisherman <= 6:
        boat_rent = boat_rent * 0.9
    elif fisherman <= 11:
        boat_rent = boat_rent * 0.85
    elif fisherman > 11:
        boat_rent = boat_rent * 0.75

if season == "Spring" or season == "Summer" or season == "Winter":
    if fisherman % 2 == 0:
        boat_rent = boat_rent * 0.95

difference = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")



