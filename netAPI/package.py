#! /usr/bin/env python
#-*-coding: utf-8-*


import pickle


CREATE_RECORD_PACKAGE_METHOD_TYPE   = 1
FIND_RECORDS_PACKAGE_METHOD_TYPE    = 2
REMOVE_RECORD_PACKAGE_METHOD_TYPE   = 3
UPDATE_RECORD_PACKAGE_METHOD_TYPE   = 4
CLOSE_CONNECT_PAKCAGE_METHOD_TYPE   = 5
RESULT_REQUEST_PAKCAGE_TYPE         = 6
CLOSE_APPLICATION_PACKAGE_TYPE      = 7
SUCCESSFUL_PACKAGE_RESULT           = 8




def serialization(package):
    return pickle.dumps(package)


def deserialization(bytes_arr):
    return pickle.loads(bytes_arr)


def make_close_connect_package():
    return Package(CLOSE_CONNECT_PAKCAGE_METHOD_TYPE)

    
def make_close_app_package():
    return Package(CLOSE_APPLICATION_PACKAGE_TYPE)

def make_package(package, method_type, data):
    package.set_method_type(method_type)
    package.set_date(data)

class Package:

    def __init__(self, method_type = None, data = str()):
        self.__pakcage_method_type  = method_type
        self.__package_data         = data


    def set_method_type(self, method_type):
        self.__pakcage_method_type = method_type


    def set_data(self, data):
        self.__package_data = data


    def get_method_type(self):
        return self.__pakcage_method_type


    def get_data(self):
        return self.__package_data