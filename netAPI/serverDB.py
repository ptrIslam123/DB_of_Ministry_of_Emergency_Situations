#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket
import sys

import newtVars as nvars
from package import *


sys.path.append('../src/')
from record import Record
from dbDriver import DBDriver
from errorHandler import ErrorHandler
import vars
import loger



class TCPServer:

    def __init__(self):
        self.__errHandler   = ErrorHandler()
        self.__record       = Record()
        self.__dbDriver     = DBDriver()

        self.__sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.__sock.bind((
            nvars.SERVER_IP_ADDRESS,
            nvars.SERVER_PORT
        ))

        


    def main_loop(self):
        self.__sock.listen(nvars.SERVER_MAX_CONNECTIONS)

        while True:
            try:
                clinet_sock, addr = self.__sock.accept()

            except KeyboardInterrupt:
                clinet_sock.close()
                break

            else:
                pkg = self.__recive_data(clinet_sock)

                if pkg.get_method_type() == CLOSE_CONNECT_PAKCAGE_METHOD_TYPE:
                    clinet_sock.close()
                    continue

                elif pkg.get_method_type() == CLOSE_APPLICATION_PACKAGE_TYPE:
                    clinet_sock.close()
                    self.__sock.close()
                    print("__exit__")
                    exit(0)

                else:
                    response_pkg = self.__exec_request(pkg)
                        
                    self.__send_data(
                        clinet_sock, 
                        response_pkg
                    )



    def __exec_request(self, package):
        method_type = package.get_method_type()
    
        if method_type == CREATE_RECORD_PACKAGE_METHOD_TYPE:
            strRecod    = package.get_data()
            data        = strRecod.split('\n')

            self.__record.convListToRecord(data)
            res = self.__dbDriver.write_new_record(self.__record)

            return Package(SUCCESSFUL_PACKAGE_RESULT, res)


        elif method_type == FIND_RECORDS_PACKAGE_METHOD_TYPE:
            #
            return Package(RESULT_REQUEST_PAKCAGE_TYPE)


        elif method_type == UPDATE_RECORD_PACKAGE_METHOD_TYPE:
            #
            return Package(RESULT_REQUEST_PAKCAGE_TYPE)


        elif method_type == REMOVE_RECORD_PACKAGE_METHOD_TYPE:
            #
            return Package(RESULT_REQUEST_PAKCAGE_TYPE)


        else:
            return Package(
                        ERROR_REQUEST_PACKAGE_TYPE,
                        self.__errHandler.handle(ERROR_REQUEST_PACKAGE_TYPE, "__server__")
                    ) 



    def __send_data(self, client_sock, package):
        client_sock.send(
            serialization(package)
        )


    def __recive_data(self, client_sock):
        pkg = deserialization(
            client_sock.recv(nvars.SERVER_DATA_BUF_SIZE)
        )
        return pkg
    

    

    
        


def main():
    server = TCPServer()
    server.main_loop()




if __name__ == "__main__":
    main()