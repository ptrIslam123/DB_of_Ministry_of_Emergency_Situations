#! /usr/bin/env python
#-*-coding: utf-8-*-


ERROR_REPOPT_FILE_NOT_FOUND                     = 1
ERROR_UNDEFINE_REQUEST_METHOD_TYPE              = 2
ERROR_SEND_PACKAGE_ON_THE_SERVER                = 3
ERROR_RECIVE_POACKAGE_FROM_SERVER               = 5
ERROR_REQUEST_PACKAGE_TYPE                      = 7
ERROR_FIND_RECORDS_IN_DB_TYPE                   = 8
AUTORIZATION_ERORR                              = 9
CLIENT_CONNECT_ERORR_TYPE                       = 10


class ErrorHandler:

    def __init__(self):
        pass


    def handle(self, err_code, obj, descrt=str()):
        if err_code == ERROR_REPOPT_FILE_NOT_FOUND:
            return "Error: report file not found "

        elif err_code == ERROR_UNDEFINE_REQUEST_METHOD_TYPE:
            return "Error: undefine request method on the server"

        elif err_code == ERROR_SEND_PACKAGE_ON_THE_SERVER:
            return "Error: error sending data to the server"

        elif err_code == ERROR_RECIVE_POACKAGE_FROM_SERVER:
            return "Error: error reciving data from the server"

        elif err_code == ERROR_REQUEST_PACKAGE_TYPE:
            return "Erorr: error client request"
        
        elif err_code == ERROR_FIND_RECORDS_IN_DB_TYPE:
            return "Error: records not found"

        elif err_code == AUTORIZATION_ERORR:
            return "Error: autorization error"

        elif err_code == CLIENT_CONNECT_ERORR_TYPE:
            return "Error: connection error to the server"

        else:
            return "Undefine error"
        