clock = int(input())
day = str(input())

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday":
    if 18 >= clock >= 10:
        print("open")
    else:
        print("closed")
else:
    print("closed")

