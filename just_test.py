#!/usr/bin/env python

print("test test")

# 打印多行的两种方法
print('''
when time is out
people wanna to die for me
hahah all of the story is joke''')

print("""
when time is out
people wanna to die for me
hahah all of the story is joke""")

# print("""
# what is happening here？
# can somebody tell me why?
# it\'s interesting!""")

# 关于变量
x = "fuck"
y = "you"
z = x + " " + y
print(type(z))
print("\n" + z)

height1 = input("Enter your height:")
weight1 = input("Enter your weight:")


def calculate_bmi(height, weight):
    if height is str or weight is str:
        print("Please input number!")
    else:
        bmi = float(weight) / (float(height) ** 2)
        print("%.1f" % bmi)
    if bmi > 32:
        print("You are so fat")
    elif 28 < bmi <= 32:
        print("obesity")
    elif 25 < bmi <= 28:
        print("overweight")
    elif 18.5 < float(bmi) <= 25:
        print("normal")
    else:
        print("slim")


calculate_bmi(height1, weight1)
