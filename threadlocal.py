#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import random
import threading
from time import sleep

from LearnPython.cat import Cat

local_cat= threading.local()


def process_cat():
    if threading.current_thread().name == 'Thread-S':
        local_cat.cat.set_name('囧大爷')
    else:
        local_cat.cat.set_name('囧二爷')
    cat = local_cat.cat
    print('%s is a cute cat! (in %s)' % (cat.get_name(), threading.current_thread().name))
    sleep(random.random())


def process_thread(cat):
    local_cat.cat = cat
    print("cat's name is %s" % cat.get_name)
    sleep(random.random())
    process_cat()


t1 = threading.Thread(target=process_thread,args=(Cat('豆豆', 'test', 14) ,), name='Thread-Q')
t2 = threading.Thread(target=process_thread,args=(Cat('毛毛', 'test', 14) ,), name='Thread-S')

t1.start()
t2.start()
t1.join()
t2.join()