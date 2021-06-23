#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket
from threading import Thread, Lock, current_thread
import sys

import netVars as nvars
from package import *


sys.path.append('../src/')
from record import Record
from dbDriver import DBDriver
from errorHandler import ErrorHandler
import vars
import loger



class TCPServer:

    def __init__(self):

        self.__dbLock       = Lock()

        self.__errHandler   = ErrorHandler()
        self.__record       = Record()
        self.__dbDriver     = None

        self.__sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        self.__sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.__bind_scoket()

        

    def __bind_scoket(self):
        try:
            self.__sock.bind((
                nvars.SERVER_IP_ADDRESS,
                nvars.SERVER_PORT
            ))

        except socket.error as e:
            loger.net_write_log(nvars.NET_SCOKET_BIND_ERROR_TYPE_EVENT, str(e))
            exit(-1)


    def main_loop(self):
        self.__sock.listen(nvars.SERVER_MAX_CONNECTIONS)

        while True:
            try:
                client_sock, addr = self.__sock.accept()
                loger.net_write_log(nvars.NET_NEW_CONNECT_EVENT, "ip address: {addr}".format(addr=addr))
                print("___NEW_CONNECT___\n")

            except KeyboardInterrupt:
                #client_sock.close()
                self.__sock.close()
                loger.net_write_log(nvars.NET_CLOSE_CONNECTION_EVENT, "KeyboardInterrupt task")
                print("___SERVER_KILL___\n")
                break
            
            except Exception:
                loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, nvars.NET_UNDEFINE_ERROR)
                #client_sock.close()
                self.__sock.close()
                print("___SERVER_FAIL__\n")
                break

            else:
                
                request_pkg, res = self.__recive_package(client_sock)

                if res != 0:
                    loger.net_write_log(nvars.NET_CREATE_NEW_TASK_EVENT, "{type_error}: {addr}".format(
                        type_error=nvars.NET_SCOKET_RECIVE_PACKAGE_ERROR, addr=addr)
                    )
                    continue

                else:
                    self.__create_new_task(client_sock, request_pkg)
                    loger.net_write_log(nvars.NET_CLOSE_CONNECTION_EVENT, "ip address: {addr}".format(addr=addr))
                    print("___CLOSE_CONNECTION___\n")



    def __create_new_task(self, client_sock, request_pkg):
        loger.net_write_log(nvars.NET_CREATE_NEW_TASK_EVENT, "thread_id : {thread_id}".format(
            thread_id=current_thread())
        )

        new_task = Thread(
            target=self.__processing_request, 
            args=(client_sock, request_pkg)
        )

        new_task.start()
        new_task.join()
                    
        loger.net_write_log(nvars.NET_EXEC_NEW_TASK_EVENT, nvars.NET_PROCESSING_REQUEST)

        
        client_sock.close()
        
        



    def __processing_request(self, client_sock, package):

        try:
            response_pkg = self.__exec_request(package)
            self.__send_package(client_sock, response_pkg)

            print("___REQUEST_SUCCESSFUL_PROCESSING___")
            exit(0)

        except Exception as e:
            print(str(e))


    def __exec_request(self, package):
        
        self.__dbDriver = DBDriver()

        method_type = package.get_method_type()
        strRecord = str("")
        
        
        loger.net_write_log(nvars.NET_EXEC_METHOD_TYPE_TASK_EVENT, ": {method_type}".format(method_type=method_type))
        print("___EXECUTE REQUEST.METHOD_TYPE()___: ", method_type)

    
        if method_type == CREATE_RECORD_PACKAGE_METHOD_TYPE:
            return self.__exec_task_to_safely_mode(
                self.__create_new_record_request, package
            )()

        elif method_type == GET_ALL_RECORDS_FROM_DB_PACKAGE_TYPE:
             return self.__get_all_record_request()

        elif method_type == FIND_RECORDS_PACKAGE_METHOD_TYPE:
            return self.__exec_task_to_safely_mode(
                self.__find_record_request, package
            )()


        elif method_type == UPDATE_RECORD_PACKAGE_METHOD_TYPE:
            return self.__exec_task_to_safely_mode(
                self.__update_record_request, package
            )()


        elif method_type == REMOVE_RECORD_PACKAGE_METHOD_TYPE:
            return self.__exec_task_to_safely_mode(
                self.__remove_record_request, package
            )()

        elif method_type == ICMP_PACKAGE_TYPE:
            return self.__exec_task_to_safely_mode(
                self.__make_icmp_package, package
            )()

        else:
            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, "{error_type}: {method_type}".format(
                error_type=nvars.NET_REQUEST_UNDEFINE_METHOD_TYPE_EVENT, method_type=method_type
            ))
            return make_erorr_package("Undefine method type")



    def __send_package(self, client, package):
        packages = split_to_list_packages(package, nvars.PACKAGE_STD_SIZE)

        for pkg in packages:
            self.__send_package_to_client(client, pkg)
            res_pkg = self.__recive_package_from_client(client)

            if res_pkg.get_method_type() != SUCCESSFUL_PACKAGE_RESULT:
                client.close()
                return -1
                
        return 0


    def __recive_package(self, client):
        packages = []

        while True:
            pkg = self.__recive_package_from_client(client)

            if pkg.get_method_type() == ERROR_REQUEST_PACKAGE_TYPE:
                loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, pkg.get_data())
                break

            if pkg.get_method_type() == LAST_PACKAGE_TYPE:
                self.__send_package_to_client(client, Package(SUCCESSFUL_PACKAGE_RESULT))
                break
            
            packages.append(pkg)

            self.__send_package_to_client(client, Package(SUCCESSFUL_PACKAGE_RESULT))
        
        return join_to_one_package(packages), 0


    def __send_package_to_client(self, client_sock, package):
        try:
            client_sock.send(
                serialization(package)
            )

            return make_successful_package()

        except socket.error as e:
            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, "socket.send method erorr: => {error_type}".format(
                error_type=e)
            )
            return make_erorr_package(str(e))
        
        


    def __recive_package_from_client(self, client_sock):
        try:
            pkg = deserialization(
                client_sock.recv(nvars.SERVER_DATA_BUF_SIZE)
            )
            return pkg

        except socket.error as e:
            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, "socket.recv method erorr: => {error_type}".format(
                error_type=e)
            )
            return make_erorr_package(str(e))

        

    
    def __create_new_record_request(self, package):
        try:
            strRecod    = package.get_data()
            data        = strRecod.split('\n')
            
            self.__record.convListToRecord(data)
            _, table_name = self.__dbDriver.write_new_record(self.__record)

            return Package(SUCCESSFUL_PACKAGE_RESULT, table_name)
        
        except Exception as e:
            error = "in the __create_new_record_request method error => {error_type}".format(
                    error_type=str(e)
            )

            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, error)
            return make_erorr_package(error)


    
    def __find_record_request(self, package):
        try:
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

        except Exception as e:
            error = "in the __find_record_request method error => {error_type}".format(
                    error_type=str(e)
            )

            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, error)
            return make_erorr_package(error)


    def __update_record_request(self, package):
        try:
            srtRecord   = package.get_data()
            data        = srtRecord.split('\n')
                
                
            res, table_name = self.__dbDriver.update_records_by_date_and_time(data)

            if res != 0:
                return make_erorr_package("Server: error updating records")

            return make_successful_package(table_name)

        except Exception as e:
            error = "in the __update_record_request method error => {error_type}".format(
                    error_type=str(e)
            )

            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, error)
            return make_erorr_package(error)

    
    def __remove_record_request(self, package):
        try:
            srtRecord   = package.get_data()
            data        = srtRecord.split('\n')
            
            res, table_name = self.__dbDriver.remove_records_by_date_and_time(
                data[0], data[1]
            )

            if res != 0:
                return make_erorr_package("Server: error remove records")
                
            return Package(SUCCESSFUL_PACKAGE_RESULT, table_name)

        except Exception as e:
            error = "in the __remove_record_request method error => {error_type}".format(
                    error_type=str(e)
            )

            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, error)
            return make_erorr_package(error)



    def __get_all_record_request(self):
        try:
            res = self.__dbDriver.get_all_records_into_table()
            return Package(SUCCESSFUL_PACKAGE_RESULT, res)

        except Exception as e:
            error = "in the __get_all_record_request method error => {error_type}".format(
                    error_type=str(e)
            )

            loger.net_write_log(nvars.NET_CRITICAL_ERROR_EVENT, error)
            return make_erorr_package(error)



    def __make_icmp_package(self, package):
        return make_successful_package(package.get_data())



    def __exec_task_to_safely_mode(self, cur_task, *args):
        def run_task():
            self.__lock_db()
            res = cur_task(*args)
            self.__unlock_db()
            
            return res

        return run_task
        


    def __lock_db(self):
        self.__dbLock.acquire()


    def __unlock_db(self):
        self.__dbLock.release()



   
    

    

    
        

def main():
    print("___STRAT_SERVER___\n")
    loger.net_write_log(nvars.NET_START_SERVER_EVENT, "___RUN__SERVER___")
    server = TCPServer()
    server.main_loop()




if __name__ == "__main__":
    main()
