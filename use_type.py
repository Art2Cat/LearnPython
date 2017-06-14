#!/usr/bin/env python3

class Hello(object):
    def hello(self, name="world"):
        print('hello, %s!' %name)


h = Hello()

h.hello()

print(type(Hello))
print(type(h))


def fc(self, name='world'):
    print('fuck, %s!' %name)

# use type method create class
# first parameter: class name
# second parameter: inheritance class
# third parameter: a dict contains reference methods
Fuck = type('Fuck', (object,), dict(fuck=fc))
f = Fuck()
f.fuck()

print(type(f))