#!/usr/bin/env python3
# -*- coding=utf-8 -*-


class Test(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '%s object' % self.__class__.__name__

    def test(self):
        print('test')

t = Test('test', 44)

print(t.name)
print(t.age)

print(type(t))
print(t)
t.test()

