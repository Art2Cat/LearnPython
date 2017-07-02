#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import os

import chardet

path = os.path.abspath('.')
print(path)

dirs = os.listdir()

print(dirs)

def convert(filepath):
    print("convert ", filepath)
    with open(filepath, 'rb') as f:
        data = f.read()
        if chardet.detect(data)['encoding'] == 'GB2312':
            data2 = data.decode('GB2312').encode('utf-8')
            print(data2)
            with open(filepath, 'wb') as f2:
                f2.write(data2)
    print('convert finished!')


def explore(paths):
    for root, dirs, files in os.walk(paths):
        for file in files:
            path = os.path.join(root, os.path.basename(file))
            if '.sql' in file:
                convert(path)


def main(folder):
        if os.path.isfile(folder):
            convert(folder)
        elif os.path.isdir(folder):
            explore(folder)


if __name__ == "__main__":
    main(path)
    # explore(dirs)
