#!/usr/bin/env python3
from LearnPython.animal import Animal
from LearnPython.dog import Dog


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    # 用于限制当前类实例的动态添加属性,继承了父类的限制
    __slots__ = 'test'

    def introduce(self):
        if not self.get_name() is None and self.get_name() != '':
            print('%s is %s cat!!!' % (self.get_name(), self.get_color()))
        else:
            print('this cat have no name!')
            super().introduce()

    def run(self):
        if self.get_name() is None or self.get_name() == "":
            super().run()
        else:
            print('%s is running' % self.get_name())

    def __call__(self, *args, **kwargs):
        self.introduce()