#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

with create_query('test') as cq:
    cq.query()


@contextmanager
def loging(title, msg):
    print('Loging begin with {title}:{msg}'.format(title=title, msg=msg))
    yield
    print('Loging end with {title}:{msg}'.format(title=title, msg=msg))


if __name__ == '__main__':
    with loging('test', 'some message'):
        print('do something')
