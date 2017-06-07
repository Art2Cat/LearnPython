#!/usr/bin/env python3

import time
import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


def log(text):
    if isinstance(text, (str, float, int)):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)

            return wrapper

        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)

        return wrapper


@log("fuck")
def now():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

now()


@log
def now():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)

now()
