#!/usr/bin/env python3
from LearnPython.animal import Animal
from LearnPython.dog import Dog


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

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


cat = Cat('囧爷', 'brown')
dog = Dog('', 'yellow')
print(cat)
cat.introduce()
dog.introduce()
cat.set_name('囧大爷')
print(cat.get_name())
cat.introduce()
cat.run()
dog.run()
cat.set_name(None)
print(cat.get_name() is not None)
print(dir(cat))

print(hasattr(cat, '_Animal__name'))  # true
