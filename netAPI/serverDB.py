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
                print("___NEW_CONNECT___\n")
                    
            except KeyboardInterrupt:
                clinet_sock.close()
                break

            else:
                pkg = self.__recive_data(clinet_sock)

                if pkg.get_method_type() == CLOSE_CONNECT_PAKCAGE_METHOD_TYPE:
                    print("___CLOSE CONNECTION___\n")
                    clinet_sock.close()
                    continue

                elif pkg.get_method_type() == CLOSE_APPLICATION_PACKAGE_TYPE:
                    clinet_sock.close()
                    self.__sock.close()
                    print("___EXIT APP__\n")
                    exit(0)

                else:
                    response_pkg = self.__exec_request(pkg)
                        
                    self.__send_data(
                        clinet_sock, 
                        response_pkg
                    )
                    
                    clinet_sock.close()
                    print("___CLOSE CONNECTION___\n")



    def __exec_request(self, package):
        method_type = package.get_method_type()
        print('method_type: ',method_type)
        strRecord = ""
    
        if method_type == CREATE_RECORD_PACKAGE_METHOD_TYPE:
            strRecod    = package.get_data()
            data        = strRecod.split('\n')

            self.__record.convListToRecord(data)
            res = self.__dbDriver.write_new_record(self.__record)

            return Package(SUCCESSFUL_PACKAGE_RESULT, res)
        
        elif method_type == GET_ALL_RECORDS_FROM_DB_PACKAGE_TYPE:
            res = self.__dbDriver.get_all_records_into_table()
        
            return Package(SUCCESSFUL_PACKAGE_RESULT, res)

        elif method_type == FIND_RECORDS_PACKAGE_METHOD_TYPE:
            strRecod    = package.get_data()
            data        = strRecod.split('\n')

            status, _ , res = self.__dbDriver.find_records_by_date_and_time(data[0], data[1])
            if status != 0:
                loger.sys_write_log(
                    vars.ERROR_LOG_TYPE ,
                    self.__errHandler.handle(ERROR_FIND_RECORDS_IN_DB_TYPE)
                )
                return make_erorr_package("Server: error find records")
            
            else:
                return Package(SUCCESSFUL_PACKAGE_RESULT, res)


        elif method_type == UPDATE_RECORD_PACKAGE_METHOD_TYPE:
            srtRecord   = package.get_data()
            data        = srtRecord.split('\n')
            
            
            res = self.__dbDriver.update_records_by_date_and_time(data)

            if res != 0:
                return make_erorr_package("Server: eror updating records")

            return Package(SUCCESSFUL_PACKAGE_RESULT)


        elif method_type == REMOVE_RECORD_PACKAGE_METHOD_TYPE:
            #
            return Package(RESULT_REQUEST_PAKCAGE_TYPE)


        else:
            return make_erorr_package("Undefine method type")



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