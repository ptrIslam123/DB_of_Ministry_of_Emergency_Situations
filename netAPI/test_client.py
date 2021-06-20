#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket
import package as pk


host = "192.168.0.12"
port = 12000


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((
    host, port
))


def make_msg(msg):
    return pk.serialization(
        pk.make_icmp_packaget(msg)
    )


data = pk.make_icmp_packaget("hello")

pk.split_packages(data)