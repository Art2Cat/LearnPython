#!/usr/bin/env python3

# []包裹起来是列表解析式
L = [x * x for x in range(10)]
print(L)

# ()包裹起来是生成器,可以用next()方法调用
g = (x * x for x in range(10))

for n in g:
    print("n =", n)
    print("next()= ", next(g))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for i in fib(6):
    print(i)
