number_of_groups = int(input())
first_row = 0
second_row = 0
third_row = 0
forth_row = 0
fifth_row = 0
total_number_of_people = 0

for i in range(1, number_of_groups + 1):
    number_of_people_in_group = int(input())
    total_number_of_people += number_of_people_in_group
    if number_of_people_in_group <= 5:
        first_row += number_of_people_in_group
    elif number_of_people_in_group <= 12:
        second_row += number_of_people_in_group
    elif number_of_people_in_group <= 25:
        third_row += number_of_people_in_group
    elif number_of_people_in_group <= 40:
        forth_row += number_of_people_in_group
    else:
        fifth_row += number_of_people_in_group

percent_first_row = first_row / total_number_of_people * 100
percent_second_row = second_row / total_number_of_people * 100
percent_third_row = third_row / total_number_of_people * 100
percent_forth_row = forth_row / total_number_of_people * 100
percent_fifth_row = fifth_row / total_number_of_people * 100
print(f"{percent_first_row:.2f}%")
print(f"{percent_second_row:.2f}%")
print(f"{percent_third_row:.2f}%")
print(f"{percent_forth_row:.2f}%")
print(f"{percent_fifth_row:.2f}%")

