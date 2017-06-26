#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import multiprocessing
import os
import time
import random
from multiprocessing import Process, Queue

from LearnPython.cat import Cat


def queue_put(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def queue_get(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
        time.sleep(random.random())


def pipe_send(p):
    print('Process to send: %s' % os.getpid())
    for value in ['Hello', '囧大爷', 13, Cat('test', 'test', 1)]:
        print('send %s to pipe...' % value)
        p.send(value)
        time.sleep(random.random())


def pipe_recv(p):
    print('Process to receive: %s' % os.getpid())
    while True:
        value = p.recv()
        print('receivce %s from pipe.' % value)
        time.sleep(random.random())


if __name__ == '__main__':
    q = Queue()
    qp = Process(target=queue_put, args=(q,))
    qg = Process(target=queue_get, args=(q,))

    p = multiprocessing.Pipe()
    ps = Process(target=pipe_send, args=(p[0],))
    pr = Process(target=pipe_recv, args=(p[1],))

    # start process
    qp.start()
    qg.start()
    ps.start()
    pr.start()

    # waiting put and send process close
    qp.join()
    ps.join()

    time.sleep(random.random())
    # force terminate receive and get process
    pr.terminate()
    qg.terminate()
