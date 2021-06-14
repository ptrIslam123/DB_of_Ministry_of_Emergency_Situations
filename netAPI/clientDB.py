#! /usr/bin/env python
#-*-coding: utf-8-*-


import socket
import sys

import newtVars as nvars
from package import *


sys.path.append('../src/')



class TCPClinet:

    def __init__(self, ip_addr, port):

        self.__sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM    
        )

        self.__sock.connect((
            ip_addr, port
        ))





    def send_data(self, package):
        self.__sock.send(
            serialization(package)
        )


    def recive_data(self):
        pkg = deserialization(
            self.__sock.recv(nvars.CLIENT_DATA_BUF_SIZE)
        )

        return pkg


    def destroy_connect(self):
        self.__sock.close()



def make_TCPClient():
    return TCPClinet(
        nvars.SERVER_IP_ADDRESS, 
        nvars.SERVER_PORT
    )



def main():
    client = make_TCPClient()

    client.send_data(
        Package(ICMP_PACKAGE_TYPE, "тестовые данные!")
    )

    
    res_pkg = client.recive_data()

    if res_pkg.get_method_type() != SUCCESSFUL_PACKAGE_RESULT:
        print("__error response__!!!")

    else:
        print(res_pkg.get_data())

 
    client.destroy_connect()
    print("__close connection__")


if __name__ == "__main__":
    main()