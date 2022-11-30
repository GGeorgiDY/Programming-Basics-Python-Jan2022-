name = input()

year = 1
sum_of_all_marks = 0
fail_counter = 0

while year <= 12:
    if fail_counter > 1:
        break
    grade = float(input())
    if grade < 4:
        fail_counter += 1
        continue # kazvame mu ne prodalvawai napred a cheti pak cikyla
    sum_of_all_marks += grade
    year += 1

if fail_counter > 1:
    print(f"{name} has been excluded at {year} grade")
else:
    average_mark = sum_of_all_marks / (year -1)
    print(f"{name} graduated. Average grade: {average_mark:.2f}")

