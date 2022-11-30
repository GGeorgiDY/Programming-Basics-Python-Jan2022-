n = int(input())
number = 0
for i in range(0, n + 1): # (n+1)
    for y in range(0, n + 1):
        for x in range(0,n + 1):
            if i + y + x == n:
                number += 1
print(number)

