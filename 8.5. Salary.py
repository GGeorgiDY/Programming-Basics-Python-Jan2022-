# number_of_open_websites = int(input())
# salary = float(input())
# penalty = 0
# website = ""
# for i in range(1, number_of_open_websites + 1):
#     website = input()
#     if website == "Facebook":
#         penalty += 150
#         if salary <= penalty:
#             print("You have lost your salary.")
#             break
#     elif website == "Instagram":
#         penalty += 100
#         if salary <= penalty:
#             print("You have lost your salary.")
#             break
#     elif penalty == "Reddit":
#         penalty += 50
#         if salary <= penalty:
#             print("You have lost your salary.")
#             break
# difference = abs(salary - penalty)
# print(difference)
number_of_open_websites = int(input())
salary = float(input())
penalty = 0
website = ""
for i in range(1, number_of_open_websites + 1):
    website = input()
    if website == "Facebook":
        penalty += 150
    elif website == "Instagram":
        penalty += 100
    elif penalty == "Reddit":
        penalty += 50
    if penalty >= salary:
        break
difference = abs(salary - penalty)
if penalty >= salary:
    print("You have lost your salary.")
else:
    print(f"{difference:.0f}")
