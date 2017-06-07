#!/usr/bin/env python3


def calculate_bmi(height, weight):
    if height is str or weight is str:
        print("Please input number!")
    else:
        bmi = float(weight) / (float(height) ** 2)
        print("%.1f" % bmi)
        if int(bmi) > 32:
            print("You are so fat")
        elif 28 < int(bmi) <= 32:
            print("obesity")
        elif 25 < int(bmi) <= 28:
            print("overweight")
        elif 18.5 < float(bmi) <= 25:
            print("normal")
        else:
            print("slim")
