#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os

import chardet
import re


path = os.path.abspath('.')
print(path)


# dirs = os.listdir()

# print(dirs)


def convert(filepath):
    print("convert ", filepath)
    with open(filepath, 'rb') as f:
        data = f.read()
        result = chardet.detect(data).get('encoding')
        if result is None:
            pass
        elif result.upper() == 'UTF-8':
            print('skip!')
        elif result.upper() == 'GB2312':
            write_to_utf8(filepath, data, result)
            print('convert finished!')
        elif result.upper() == 'GB18030':
            write_to_utf8(filepath, data, result)
            print('convert finished!')
        elif result.upper() == 'GBK':
            write_to_utf8(filepath, data, result)
            print('convert finished!')
        elif result.upper() == 'ASCII':
            write_to_utf8(filepath, data, result)
            print('convert finished!')
            # else:
            # write_to_utf8(filepath, data, 'unicode')
            # print('convert finished!')


def write_to_utf8(filepath, origin_data, origin):
    data = origin_data.decode(origin).encode('utf-8')
    with open(filepath, 'wb') as f:
        f.write(data)


# convert(path1)


def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, os.path.basename(file))
            if check_file(file):
                convert(path)


def check_file(file):
    rex = re.compile(r'([a-zA-Z0-9+_\-*\\/]*)\.([a-zA-Z0-9]*)')

    result = rex.match(str(file))
    if result is None:
        return False
    if len(result.groups()) == 0:
        return False
    return True


def main(dir):
    if os.path.isfile(dir):
        convert(dir)
    elif os.path.isdir(dir):
        explore(dir)


if __name__ == "__main__":
    main(path)
    # explore(dirs)
