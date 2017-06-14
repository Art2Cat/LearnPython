# !/usr/bin/env python3

"a test module"

import sys

from utils.util import log

__author__ = 'Art2Cat'


@log('execute')
def hello_world():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    hello_world()
