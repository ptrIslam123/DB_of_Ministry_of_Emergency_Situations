
#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket
import package as pk


host = "192.168.0.12"
port = 12000


server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
)

server.bind((
        host, port
))

server.listen(5)


while True:
        try:
                client, addr = server.accept()

        except KeyboardInterrupt:
                server.close()
                break

        else:
                try:
                        result = None
                        while True:
                                data = client.recv(1024)

                        

                except KeyboardInterrupt:
                        client.close()
                        break