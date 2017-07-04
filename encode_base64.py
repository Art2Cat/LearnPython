#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import base64

s = '测试'

b = s.encode('utf-8')
print(b)

b64 = base64.b64encode(b)

print(b64)

b2 = base64.b64decode(b64)
print(b2)

s = b2.decode('utf-8')
print(s)

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))

print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

print(base64.urlsafe_b64decode('abcd--__'))

poet = b'6Iuf5Yip5Zu95a6255Sf5q275Lul77yM5bKC5Zug56W456aP6YG/6LaL5LmL44CC'

t = base64.b64decode(poet).decode('utf-8')
print(t)


def safe_base64_decode(s):
    return base64.b64decode(s + b'=' * (4 - len(s) % 4))

print(safe_base64_decode(b'YWJjZA=='))