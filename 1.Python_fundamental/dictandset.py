#!/usr/bin/env python


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d['Bob'])

if "Thomas" in d:
    print(d.get('Thomas'))
else:
    print("None")

d['Thomas'] = 64

if "Thomas" in d:
    print(d.get('Thomas'))
else:
    print("None")

print(sorted(d))

s = set([1, 2, 3, 4])
s1 = set([5, 6, 4])
s.add(6)

print(s)
print(s & s1)
print(s | s1)
