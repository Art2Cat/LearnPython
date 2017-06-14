#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from cat import Cat
from dog import Dog

cat = Cat('囧爷', 'brown')
dog = Dog('', 'yellow')
print(cat)
# cat()
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

try:
    dog.test = 'test success'
except Exception as e:
    print(e)
else:
    print("no error!!!")
finally:
    print("finally...")

print(dog.test)

print(hasattr(cat, 'test2'))
print(hasattr(dog, 'test'))

print('' is None)
