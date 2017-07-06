#!/user/bin/env python3
# -*- coding=utf-8 -*-
import asyncio
import threading


# 通过装饰器把hello()标记为coroutine类型
@asyncio.coroutine
def hello():
    print("Hello world (%s)" % threading.currentThread())
    # 异步调用asyncio.sleep(1)
    yield from asyncio.sleep(1)
    print("Fuck you! (%s)" % threading.currentThread())


# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))


# loop.close()


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


tasks1 = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks1))
loop.close()
