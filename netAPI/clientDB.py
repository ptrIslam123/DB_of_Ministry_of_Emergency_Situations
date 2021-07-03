#! /usr/bin/env python
#-*-coding: utf-8-*-


import socket
import sys

import netVars as nvars
from package import *
import test_client as tclient

sys.path.append('../src/')
import errorHandler
import loger 


class TCPClinet:

    def __init__(self, ip_addr, port):

        
        self.__ip_addr = ip_addr
        self.__port = port

        self.__sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM    
        )

        
        

    def connect(self):
        try:
            self.__sock.connect((
                self.__ip_addr, self.__port
            ))

            return 0

        except socket.error as e:
            loger.sys_write_log(nvars.NET_CLIENT_CONNECT_ERROR_TYPE__EVENT, str(e))
            return errorHandler.CLIENT_CONNECT_ERORR_TYPE


    def send_package(self, package):
        packages = split_to_list_packages(package, nvars.PACKAGE_STD_SIZE)

        for pkg in packages:
            self.__send_package_to_server(pkg)
            res_pkg = self.__recive_package_from_server()
            
            if res_pkg.get_method_type() != SUCCESSFUL_PACKAGE_RESULT:
                self.__sock.close()
                return -1
            
        return 0


    def recive_package(self):
        packages = []

        while True:
            pkg = self.__recive_package_from_server()

            if pkg.get_method_type() == LAST_PACKAGE_TYPE:
                self.__send_package_to_server(Package(SUCCESSFUL_PACKAGE_RESULT))
                break
            
            packages.append(pkg)

            self.__send_package_to_server(Package(SUCCESSFUL_PACKAGE_RESULT))
        
        return join_to_one_package(packages), 0


    def __send_package_to_server(self, package):
        try:
            self.__sock.send(
                serialization(package)
            )

            return 0

        except socket.error as e:
            loger.sys_write_log(nvars.NET_CRITICAL_ERROR_EVENT, "socket.send method error: {error_type}".format(
                error_type=str(e)
            ))
            return -1



    def __recive_package_from_server(self):
        try:
            pkg = deserialization(
                self.__sock.recv(nvars.CLIENT_DATA_BUF_SIZE)
            )

            return pkg

        except socket.error as e:
            loger.sys_write_log(nvars.NET_CRITICAL_ERROR_EVENT, "socket.recv method error: {error_type}".format(
                error_type=str(e)
            ))
            return make_erorr_package(str(e))



    def destroy_connect(self):
        self.__sock.close()



def make_TCPClient():
    return TCPClinet(
        nvars.SERVER_IP_ADDRESS, 
        nvars.SERVER_PORT
    )



def main():
    client = TCPClinet(
        nvars.SERVER_IP_ADDRESS, 
        nvars.SERVER_PORT
    )

    if client.connect() != 0:
        print("connect error!")
        exit(-1)

    res_pkg = tclient.test_icmp(client, "hello world!")
    print(res_pkg.get_data())

if __name__ == "__main__":
    main()