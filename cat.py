#!/usr/bin/env python3

class Cat(object):
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def introduce(self):
        print('%s is %s cat!!!' % (self.__name, self.__color))

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

cat = Cat('囧爷', 'brown')

print(cat)
cat.introduce()
cat.set_name('囧大爷')
print(cat.get_name())
cat.introduce()


