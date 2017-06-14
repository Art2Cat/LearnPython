#!/usr/bin/env python3
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

r1 = reduce(exponentiation, [2, 2, 3, 4])

print(r1)


def add1(x, y):
    return x + y


def fn(x, y):
    return x * 10 + y


r2 = reduce(fn, [1, 2, 3, 4, 5, 6])

print(r2)


def str2int(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9}[s]
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


s = "9527"

print(str2int(s))


def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9}[s]
    s1, s2 = s.split('.')
    return reduce(lambda x, y: x * 10 + y, map(char2num, s1)) + \
        reduce(lambda x, y: x * 10 + y, map(char2num, s2)) / pow(10, len(s2))


s = "9527.9527"

print(str2float(s))


def is_palindrome(n):
    while n >= 10:
        if str(n % 10) != str(n)[0]:
            return False
        n = int(str(n)[1:]) // 10
    return True


output = filter(is_palindrome, range(1, 1000))

print(list(output))


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(by_name(L))
L2 = sorted(L, key=by_name)
L1 = sorted(L, key=by_score, reverse=True)
print(L2)
print(L1)
