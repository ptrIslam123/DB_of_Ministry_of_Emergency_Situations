#! /usr/bin/env python
#-*-coding: utf-8-*-


import socket
import sys

import newtVars as nvars
from package import *


sys.path.append('../src/')
from record import Record


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



def main():
    client = TCPClinet(
        nvars.SERVER_IP_ADDRESS,
        nvars.SERVER_PORT
    )

    client.send_data(
        Package(CREATE_RECORD_PACKAGE_METHOD_TYPE, "тестовые данные!")
    )

    res_pkg = client.recive_data()

    if res_pkg.get_method_type() != RESULT_REQUEST_PAKCAGE_TYPE:
        print("__error response__!!!")

    else:
        print(res_pkg.get_data())
        client.send_data(
            make_close_connect_package()
        )

        print("__close connection__") 



    client.destroy_connect()


if __name__ == "__main__":
    main()