#!/usr/bin/env python

lists = []
for i in range(10):
    lists.insert(i, i)
print(lists)

lists.clear()
lists = [i for i in range(10)]

for i in range(10):
    lists.append(i)

print(lists)
print(lists[-3:])
print("lists lenth %d" % len(lists))

t = (1, 2, 1, 3, lists)
print(t)
t[4][0] = 'X'
t[-1][1] = 'Y'
print(t)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][1])
print(L[1][1])
print(L[2][2])
