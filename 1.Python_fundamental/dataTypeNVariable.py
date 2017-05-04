#!/usr/bin/env python

i = 25
f = 15.5
s = "This is String"
b = True

print(type(i))
print(type(f))
print(type(s))
print(type(b))

# print multi-line
print('''
when time is out
people wanna to die for me
hahah all of the story is joke''')

print("""
when time is out
people wanna to die for me
hahah all of the story is joke""")

# Escape character '\'
print("She said: \"What's wrong?\"")

# not and or
print(not True)
print(True or False)
print(s is str and i is not float)

# math operator
z = 10 / 3
print("%f" % z)
# console: 3.333333

z = 12 / 3.0
print("%.1f" % z)
# console: 4.0

z = 10 // 3
print("%d" % z)
# console: 3

# powers operator '**'
z = 2 ** 3
print(z)
# console: 8
