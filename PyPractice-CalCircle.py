# PyPractice-CircleAreaCalculation

import math

r = eval(input("圆的半径："))
if (r >= 0):
    area = math.pi * pow(r, 2)
else:
    print("请输入正确半径")

print("圆的面积的面积是{:.2f}".format(area))
