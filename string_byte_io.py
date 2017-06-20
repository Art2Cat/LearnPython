#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from io import BytesIO, StringIO

f = StringIO()

f.write('hello')

print(f.getvalue())


fi = StringIO('Hello!\nHi!\nGoodbye!')

while True:
    s = fi.readline()
    if s == '':
        break
    print(s.strip())


fil = BytesIO()

fil.write('中文'.encode('utf-8'))

print(fil.getvalue())
