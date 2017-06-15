#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from cat import Cat
from dog import Dog

cat = Cat('囧爷', 'brown', 2)
dog1 = Dog.age('wang', 'brown', 2)
dog = Dog('', 'yellow')
print(cat)
print(dog1)
cat()

Dog.bark('wang wang wang')

cat.introduce()
dog.introduce()
cat.set_name('囧大爷')
print(cat.get_name())
cat.set_color(None)
print(not isinstance(cat.get_color(), str) or not cat.get_color())
cat.introduce()
cat.run()
dog.run()
print(dir(cat))

print(hasattr(cat, '_Animal__name'))  # true

try:
    cat.test2 = 'test failed'
except Exception as e:
    print("Exception: ", e)
else:
    print("no error!!!")
finally:
    print("finally...")

dog1.test = 'test success'

print(hasattr(cat, 'test2'))  # false
print(hasattr(dog1, 'test'))  # true

del dog1.test  # delete instance dog1's property
print(hasattr(dog1, 'test'))  # false
