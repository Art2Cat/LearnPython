#!/usr/bin/env python3

import os

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for k, v in d.items():
    print("%s : %.2d" % (k, v))


for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print([d for d in os.listdir('.')])

print([k + '=' + str(v) for k, v in d.items()])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str)]
print(L2)
