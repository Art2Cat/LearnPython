#!/usr/bin/env python3


class Student(object):

    def __len__(self):
        return 256

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth


s = Student()
s.birth = 1989



x = s.birth


print(hasattr(s, '_birth'))
print(x)
print(len(s))
print(s.age)
