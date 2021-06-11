#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket


s = socket.socket()

host = socket.gethostname()
port = 12000

s.bind((host, port))

s.listen(5)

while True:

    c, addr = s.accept()
    print 'получить сообщение от ', addr
    c.send('спасибо за подключение')
    c.close()
        