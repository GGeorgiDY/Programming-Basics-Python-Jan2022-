first_num = int(input())
second_num = int(input())
third_num = int(input())
total = first_num + second_num + third_num
minutes = total // 60
seconds = total % 60
# print(f"{minutes}:{seconds:02d}")
if seconds <= 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
