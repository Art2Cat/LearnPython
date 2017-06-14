#!/usr/bin/env python3
class Animal(object):
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    # self.__class__.__name__ 获取当前类的名字
    # __str__
    def __str__(self):
        return '%s object (name: %s)' %(self.__class__.__name__, self.__name)

    __repr__ = __str__

    # 用于限制当前类实例的动态添加属性
    __slots__ = ('__name', '__color')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def run(self):
        print('Animal is running...')

    def introduce(self):
        print('%s is %s Animal!!!' % (self.get_name(), self.get_color()))
