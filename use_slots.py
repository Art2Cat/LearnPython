#!/usr/bin/env python3
from LearnPython.cat import Cat
from LearnPython.dog import Dog

cat = Cat('囧爷', 'brown')
dog = Dog('', 'yellow')
print(cat)
cat()
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
print(cat.test2)
