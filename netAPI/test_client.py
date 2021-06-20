#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket
from package import *

host = "192.168.0.12"
port = 12000


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((
    host, port
))

pkg = Package(CREATE_RECORD_PACKAGE_METHOD_TYPE, "hello my new package data!")

pkgs = split_to_list_packages(pkg, 5)

while True:
    try:
        data = raw_input(">")

        if data == "end":
            client.send(serialization(
                Package(LAST_PACKAGE_TYPE, "connect destroy[client]")
            ))

            pkg = deserialization(client.recv(1024))
            print("__close connect__: ", pkg.get_data())
            break
        
        client.send(serialization(
            Package(ICMP_PACKAGE_TYPE, data=data)
        ))

        pkg = deserialization(client.recv(1024))
        print("type: ", pkg.get_method_type(), 'data: ' ,pkg.get_data())

    except KeyboardInterrupt:
        client.close()
        break



client.close()


'''
while True:
    try:
        client.send(serialization(
            Package(ICMP_PACKAGE_TYPE, raw_input(">"))
        ))

        pkg = deserialization(client.recv(1024))
        print("type: ", pkg.get_method_type(), 'data: ', pkg.get_data())

    except KeyboardInterrupt:
        client.close()
        break



client.close()
'''