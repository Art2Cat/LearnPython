#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

naturals = itertools.count(1)
for n in naturals:
    print(n)
    if n >= 10:
        break

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break

rp = itertools.repeat('fuck you', 3)
for n in rp:
    print(n)

gb = itertools.groupby('tTTeEEEsSSttesSStAaabbccddsssa', lambda x: x.lower())
for k, g in gb:
    print(k, list(g))

for x, y in itertools.groupby('111246497746447761'):
    print(x, list(y))
