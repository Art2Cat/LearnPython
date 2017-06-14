#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from animal import Animal


class Cat(Animal):
    def __init__(self, name, color, age):
        super(Cat, self).__init__(name, color)
        self.age = age

    # 用于限制当前类实例的动态添加属性,继承了父类的限制
    __slots__ = ('test', 'age')

    def __call__(self, *args, **kwargs):
        self.introduce()
