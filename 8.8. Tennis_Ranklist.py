import math

number_of_tournaments = int(input())
initial_points = int(input())
points_during_the_season = 0
won_tournaments = 0

for i in range(1, number_of_tournaments +1):
    rang = input()
    if rang == "W":
        points_during_the_season += 2000
        won_tournaments += 1
    elif rang == "F":
        points_during_the_season += 1200
    elif rang == "SF":
        points_during_the_season += 720

final_points = math.floor(initial_points + points_during_the_season)
average_points = math.floor(points_during_the_season / number_of_tournaments)
percent_of_won_tournaments = won_tournaments / number_of_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_of_won_tournaments:.2f}%")

