#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import multiprocessing
import time

import aiohttp
import asyncio
import requests
import threadpool as threadpool

test_url = 'http://www.qq.com'


class Requests(object):
    def run(url):
        r = requests.get(url=url)


class SingleProcess(object):
    @classmethod
    def run(cls, url):
        start_time = time.time()
        for x in range(100):
            requests.get(url)
        print("用时：{}秒".format(time.time() - start_time))


class MultiProcess(Requests):
    @classmethod
    def benchmark(cls, url):
        start_time = time.time()
        pool = multiprocessing.Pool(10)
        for x in range(100):
            pool.apply_async(cls.run, args=(url))
        pool.close()
        pool.join()
        print("用时：{}秒".format(time.time() - start_time))


class MultiThread(Requests):
    @classmethod
    def benchmark(cls, url):
        start_time = time.time()
        pool = threadpool.ThreadPool(10)
        reqs = threadpool.makeRequests(
            cls.run, [url for x in range(100)])
        for x in reqs:
            pool.putRequest(x)
        pool.wait()
        print("用时：{}秒".format(time.time() - start_time))


class AsyncIO(object):
    async def run(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as resp:
                pass

    @classmethod
    def benchmark(cls, url):
        start_time = time.time()
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(
            cls.run(url)) for x in range(100)]
        loop.run_until_complete(asyncio.wait(tasks))
        print("用时：{}秒".format(time.time() - start_time))


def benchmark():
    mode = input('enter benchmark mode: ')
    if mode == 'exit':
        print('exit benchmark')
    elif mode == 'single':
        SingleProcess.run(test_url)
        benchmark()
    elif mode == 'multiP':
        MultiProcess.benchmark(test_url)
        benchmark()
    elif mode == 'multiT':
        MultiThread.benchmark(test_url)
        benchmark()
    elif mode == 'AIO':
        AsyncIO.benchmark(test_url)
        benchmark()
    else:
        print('exit benchmark')


benchmark()
