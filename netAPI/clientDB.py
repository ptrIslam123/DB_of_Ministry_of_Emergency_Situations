#! /usr/bin/env python
#-*-coding: utf-8-*-


import socket
import newtVars as nvars



s= socket.socket()

host = socket.gethostname()
port = 12000

s.connect((host, port))

while True:

    try:
        data = raw_input('>')
        
        if data == "close":
            s.send('close')
            print("__close connect__")
            s.close()
            break

        s.send(data)

        result = s.recv(1024)
        print 'сервер: ', result

    except KeyboardInterrupt:
        print("__close client socekt__")
        s.close()
        break





'''

s.send('привет мир!')
result = s.recv(1024)

print 'сервер: ', result
'''