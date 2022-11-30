first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    odd_digits_sum = 0
    even_digits_sum = 0
    i_as_string = str(i)
    for index, digit in enumerate(i_as_string):
        if index % 2 == 0:
            odd_digits_sum += int(digit)
        else:
            even_digits_sum += int(digit)
    if odd_digits_sum == even_digits_sum:
        print(i, end=" ")
