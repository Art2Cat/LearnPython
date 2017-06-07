# coding:utf-8
from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


print(add(10, -54, abs))


def exponentiation(x, y):
    return x ** y


def multiply(x, y, f):
    return f(x, y) * f(y, x)


print(exponentiation(2, 10))
print(multiply(2, 10, exponentiation))

r = map(exponentiation, [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

r1 = reduce(exponentiation, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(r1)


def add1(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


r2 = reduce(fn, [1, 2, 3, 4, 5, 6])

print(r2)


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))


s = "9527"

print(str2int(s))

print(pow(2, 10))
