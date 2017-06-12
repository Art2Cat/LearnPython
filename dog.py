#!/usr/bin/env python3
from LearnPython.animal import Animal


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def introduce(self):
        if self.get_name() is not None and self.get_name() != '':
            print('%s is %s dog!!!' % (self.get_name(), self.get_color()))
        else:
            print('this dog have no name!')
            super().introduce()

    def run(self):
        if self.get_name() is None or self.get_name() == "":
            super().run()
        else:
            print('%s is running' % self.get_name())
