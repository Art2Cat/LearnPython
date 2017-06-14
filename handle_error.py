#!usr/bin/env python3
import logging


class TestError(ValueError):
    pass


def divide(x, y):
    x = int(x)
    n = int(y)
    if n == 0:
        raise TestError('invalid value: %d' % n)
    return x / n


try:
    print(divide(5,2))
    print(divide(5,0.0))
except Exception as e:
    logging.exception(e)
finally:
    print("done!")


def bar():
    try:
        divide(2, '0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()