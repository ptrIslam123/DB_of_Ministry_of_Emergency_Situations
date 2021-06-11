#! /usr/bin/env python
#-*-coding: utf-8-*-


import socket
import newtVars as nvars



s= socket.socket()

host = socket.gethostname()
port = 12000

s.connect((host, port))


print s.recv(1024)
s.close()