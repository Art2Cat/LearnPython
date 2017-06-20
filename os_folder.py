#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os

# 查看当前目录的绝对路径:
x = os.path.abspath('.')
print(x)
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
y = os.path.join(x, 'testdir')
print(y)
# 然后创建一个目录:
os.mkdir(y)
# 删掉一个目录:
os.rmdir(y)
path = os.path.join(x, 'test.txt')

if os.path.exists(path):
    print("File exists")
else:
    open(path, 'a')

z = os.path.split(os.path.join(x, 'os_folder.py'))
print(z)

z = os.path.splitext(path)

print(z)

os.rename('test.txt', 'test.log')

os.remove('test.log')

files = [x for x in os.listdir('.') if os.path.isfile(
    x) and os.path.splitext(x)[1] == '.py']

for x in files:
    print(x)
