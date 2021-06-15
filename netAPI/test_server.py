
#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket


host = "192.168.0.12"
port = 12000


server = socket.socket(
      socket.AF_INET,
      socket.SOCK_STREAM  
)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((
        host,
        port
))


server.listen(5)

try:
        print("__strat_server__\n")
        while True:
                try:
                        client, addr = server.accept()
                        print("__new_connect__")
                        print(addr)
                        print("\n")
                except:
                        client.close()
                        break
                
                else:
                        request = client.recv(1024)
                        client.send(request)

                        client.close()
                        print("__close_connect__\n")
except:
        server.close()
                

