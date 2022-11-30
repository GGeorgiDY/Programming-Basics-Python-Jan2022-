number_floors = int(input())
number_rooms = int(input())
floor = 0
room = 0

for floor in range(number_floors, 0, -1):
    for room in range(0, number_rooms):
        if floor % 2 == 0:
            vid = "O"
        else:
            vid = "A"
        if floor == number_floors:
            vid = "L"
        print(f"{vid}{floor}{room} ", end="")
    print()


