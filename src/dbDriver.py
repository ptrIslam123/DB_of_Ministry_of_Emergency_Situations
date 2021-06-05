#! /usr/bin/env python
#-*-coding: utf-8-*-


from employees import Employees 
from shift import Shift 
from technic import Technic  
from brigade import Brigade 
from geographLocation import GeographLocation 


class DBDriver:

    def __init__(self):
        self.__employees            = Employees()
        self.__shift                = Shift()
        self.__technic              = Technic()
        self.__brigade              = Brigade()
        self.__geographLocation     = GeographLocation()


    def write_new_record(self, record):
        pass