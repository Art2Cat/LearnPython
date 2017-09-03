#!/usr/bin/env python3


from socket import *
from time import ctime

HOST = 'localhost'
PORT = 23333
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcp_cli_sock = socket(AF_INET, SOCK_STREAM)
tcp_cli_sock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcp_cli_sock.send(data)
    data = tcp_cli_sock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))
tcp_cli_sock.close()
