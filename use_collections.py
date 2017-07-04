#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from collections import *


# namedtuple is function
# namedtuple('name', ['attribute', 'list'])
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))


# deque
q = deque(['a', 'b', 'c'])
q.append('y')
q.appendleft('z')
print(q)


# defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'fuck'
print('key1\'s value is %s' % dd['key1'])  # fuck
print('key2\'s value is %s' % dd['key2'])  # N/A


# OrderedDict
d = {'a': 1, 'b': 2, 'd': 4, 'c': 3}
print(d)  # dict key is unordered
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict key is ordered


class FIFODict(OrderedDict):

    def __init__(self, capacity):
        super(FIFODict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

    def add(self, key, value):
        self.__setitem__(key, value)


f = FIFODict(3)
f.add('a', 1)
f.add('b', 2)
f.add('c', 3)
f.add('test', 4)
print(f)

c = Counter()
for l in 'precipitation':
    c[l] = c[l] + 1

print(c)
