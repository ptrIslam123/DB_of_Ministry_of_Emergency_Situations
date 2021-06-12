#! /usr/bin/env python
#-*-coding: utf-8-*-


ERROR_REPOPT_FILE_NOT_FOUND                     = 1
ERROR_UNDEFINE_REQUEST_METHOD_TYPE              = 2
ERROR_SEND_PACKAGE_ON_THE_SERVER                = 3
ERROR_RECIVE_POACKAGE_FROM_SERVER               = 5
ERROR_REQUEST_PACKAGE_TYPE                      = 7


class ErrorHandler:

    def __init__(self):
        pass


    def handle(self, err_code, obj, descrt=""):
        return "Error"