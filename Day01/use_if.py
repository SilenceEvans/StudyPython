import random

age = 20
# if的初级使用
"""
if之后所有带缩进的代码块都归属于if的范围
"""
if age >= 18:
    print("你可以进去")
    print("我也属于你")
else:
    print("你不能进去")

num = 15
if num > 20:
    print(num)
elif num < 18:
    print(num)

print(random.randint(1, 3))
