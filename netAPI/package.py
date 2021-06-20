#! /usr/bin/env python
#-*-coding: utf-8-*

from itertools import izip_longest
import pickle
import sys

sys.path.append('../src/')
from errorHandler import *

CREATE_RECORD_PACKAGE_METHOD_TYPE       = 1
FIND_RECORDS_PACKAGE_METHOD_TYPE        = 2
REMOVE_RECORD_PACKAGE_METHOD_TYPE       = 3
UPDATE_RECORD_PACKAGE_METHOD_TYPE       = 4
CLOSE_CONNECT_PAKCAGE_METHOD_TYPE       = 5
RESULT_REQUEST_PAKCAGE_TYPE             = 6
CLOSE_APPLICATION_PACKAGE_TYPE          = 7
SUCCESSFUL_PACKAGE_RESULT               = 8
GET_ALL_RECORDS_FROM_DB_PACKAGE_TYPE    = 9
ICMP_PACKAGE_TYPE                       = 10
LAST_PACKAGE_TYPE                       = 11




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


def make_erorr_package(message_err):
    return Package(ERROR_REQUEST_PACKAGE_TYPE, message_err)


def make_icmp_packaget(msg):
    return Package(ICMP_PACKAGE_TYPE, msg)



def split_str_data(iterable, n, fillvalue=''):
    iterable = iterable.decode('utf-8') # опционально!
    args = [iter(iterable)] * n

    ans = list(izip_longest(fillvalue=fillvalue, *args))

    for i in range(len(ans)):
        ans[i] = "".join(ans[i])


    return ans



def split_to_set_packages(package):
    packages = []

    method_type = package.get_method_type()
    data        = package.get_data() # type(str)
   
    list_data = split_str_data(data, 5)
    size_list_data = len(list_data)

    for data in list_data:
        packages.append(
            Package(method_type=method_type, data=data)
        )

    packages[size_list_data - 1].set_method_type(LAST_PACKAGE_TYPE) 
    return packages

    




def join_to_one_packages(packages):
    method_type = packages[0].get_method_type()
    data = str("")

    for p in packages:
        data += p.get_data()

    return Package(method_type=method_type, data=data)

        




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





def main():

    res = split_to_set_packages(make_icmp_packaget(
        "привет мир!|"
    ))

    pack = join_to_one_packages(res)
    print("method_type: ", pack.get_method_type())
    print(pack.get_data())
        



if __name__ == "__main__":
    main()