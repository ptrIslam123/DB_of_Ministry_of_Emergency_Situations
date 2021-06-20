
#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket
from package import *


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
                        while True:
                                
                                pkg = deserialization(client.recv(1024))
                                
                                if pkg.get_method_type() == LAST_PACKAGE_TYPE:
                                        print("__close connect__: ", pkg.get_data())
                                        client.send(serialization(
                                                Package(CLOSE_CONNECT_PAKCAGE_METHOD_TYPE, "connect destroy[server]")
                                        ))
                                        client.close()
                                        break
                                
                                print("type: ", pkg.get_method_type(), 'data: ', pkg.get_data())
                                client.send(serialization(Package(
                                        ICMP_PACKAGE_TYPE, "Ok"
                                )))

                except KeyboardInterrupt:
                        client.close()
                        break



'''
while True:
        try:
                client, addr = server.accept()

        except KeyboardInterrupt:
                server.close()
                break

        else:
                try:
                        while True:
                                
                                pkg = deserialization(client.recv(1024))
                                print("type: ", pkg.get_method_type(), 'data: ', pkg.get_data())
                                
                                client.send(serialization(Package(
                                        ICMP_PACKAGE_TYPE, "Ok"
                                )))
                                
                except KeyboardInterrupt:
                        client.close()
                        break
'''