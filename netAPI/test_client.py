#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket


host = "192.168.0.12"
port = 12000

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((
    host,
    port
))

client.send("hello world")
data = client.recv(1024)

print("response from server: ", data)

client.close()