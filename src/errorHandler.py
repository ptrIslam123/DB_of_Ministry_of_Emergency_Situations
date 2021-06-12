#! /usr/bin/env python
#-*-coding: utf-8-*-


ERROR_REPOPT_FILE_NOT_FOUND         = 1
ERROR_UNDEFINE_REQUEST_METHOD_TYPE  = 2


class ErrorHandler:

    def __init__(self):
        pass


    def handle(self, err_code, obj, descrt=""):
        return "Error"