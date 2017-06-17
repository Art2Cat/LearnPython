#!/usr/bin/env python3
# -*- coding=utf-8 -*-

path = '/Users/Rorschach/text.txt'


def origin_read_all(path):
    try:
        f = open(path, 'r')
        print(f.read())
    finally:
        if f:
            f.close()


def with_read_all(path):
    # errors='ignore' better use with encoding=''
    # if path file not exist will break "with...as.." syntax
    with open(path, 'r', errors='ignore') as f:
        print(f.read())


def read_lines(path):
    with open(path, 'r') as f:
        print(f.readlines())


def read_line(path, n):
    with open(path, 'r') as f:
        print(f.readline(n))


def read_bin(path):
    with open(path, 'rb') as f:
        print(f.readlines())


def read_with_encoding(path):
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())


def read_with_encoding1(path, encode):
    with open(path, 'r', encoding=encode, errors='ignore') as f:
        print(f.read())


def write_with_encoding(path, content, encode):
    with open(path, 'w', encoding=encode) as f:
        f.write(content)


mode = int(input('set read mode(1-8):'))

if mode == 1:
    origin_read_all(path)
elif mode == 2:
    with_read_all(path)
elif mode == 3:
    read_lines
elif mode == 4:
    n = input('read line number:')
    read_line(path, n)
elif mode == 5:
    print(mode)
    read_with_encoding(path)
elif mode == 6:
    read_bin(path)
elif mode == 7:
    c = input('write something:')
    e = input('input encode mode:')
    write_with_encoding(path, c, e)
elif mode == 8:
    e = input('input encode mode:')
    read_with_encoding1(path, e)