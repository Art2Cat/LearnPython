#!/usr/bin/env python3
import functools
import time


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


def log(text):
    if isinstance(text, (str, float, int)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                _log_time()
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            _log_time()
            print('call %s():' % text.__name__)
            return text(*args, **kw)

        return wrapper


def _log_time():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)


def equals(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError('arguments type must be <str>')
    if str1 == str2:
        return True
    return False


def is_empty(string):
    if not isinstance(string, str):
        raise TypeError('arguments type must be <str>')

    if not string:
        return True
    return False
