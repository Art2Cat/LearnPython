#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from multiprocessing import pool, Manager

from multiprocessing.pool import Pool
import time


class PageControler(object):
    def __init__(self):
        self.nProcess = 3
        self.pages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.manageWork()

    def manageWork(self):

        self.pool = Pool(processes=self.nProcess)

        time.sleep(2)
        work_queue = threading.Thread(target=self.modifyQueue)
        work_queue.start()

        # pool.close()
        # pool.join()

    def deliverWork(self):
        if self.pages != []:
            pag = self.pages.pop()
            self.pool.apply_async(self.myFun)

    def modifyQueue(self):
        t = time.time()
        while (time.time() - t) < 10:
            time.sleep(1)
            self.pages.append(99)
            print(self.pages)
            self.deliverWork()

    def myFun(self):
        time.sleep(2)

    def __getstate__(self):
        self_dict = self.__dict__.copy()
        del self_dict['pool']
        return self_dict

    def __setstate__(self, state):
        self.__dict__.update(state)


class Data(object):
    def __init__(self):
        self.pool = Pool(2)
        self.queue = Manager().Queue()

    def put(self, item):
        self.queue.put(item)

    def out(self, queue):
        while True:
            item = queue.get()
            print(item)
            time.sleep(0.01)

    def start(self):
        print(self.queue.qsize())
        for _ in range(2):
            self.pool.apply_async(self.out, (self.queue,))


if __name__ == '__main__':

    data = Data()
    for i in range(1000):
        data.put(i)
    data.start()
    data.pool.close()
    data.pool.join()
    time.sleep(5)

    manger = PageControler()
    # manger.deliverWork()
    manger.manageWork()
    manger.modifyQueue()
    manger.myFun()
