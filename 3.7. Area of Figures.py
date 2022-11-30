# Да се напише програма, в която потребителят въвежда вида и размерите на геометрична
# фигура и пресмята лицето й. Фигурите са четири вида: квадрат (square),
# правоъгълник (rectangle), кръг (circle) и триъгълник (triangle).
# На първия ред на входа се чете вида на фигурата (текст със следните възможности: square,
# rectangle, circle или triangle).
# ⦁	Ако фигурата е квадрат (square): на следващия ред се чете едно дробно число - дължина на страната му
# ⦁	Ако фигурата е правоъгълник (rectangle): на следващите два реда четат две д
# робни числа - дължините на страните му
# ⦁	Ако фигурата е кръг (circle): на следващия ред чете едно дробно число - радиусът на кръга
# ⦁	Ако фигурата е триъгълник (triangle): на следващите два реда четат две дробни
# числа - дължината на страната му и дължината на височината към нея

import math
figure = str(input())
side_a = float(input())
area = 0
if figure == "square":
    area = side_a * side_a
    print(area)
elif figure == "rectangle":
    side_b = float(input())
    area = side_a * side_b
    print(area)
elif figure == "circle":
    area = math.pi * side_a * side_a
    print(area)
elif figure == "triangle":
    h = float(input())
    area = (side_a * h) / 2
    print(area)
