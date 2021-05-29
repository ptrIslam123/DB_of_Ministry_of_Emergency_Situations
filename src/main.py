#! /usr/bin/env python
#-*-coding: utf-8-*-


from employees import Employees
from shift import Shift
from technic import Technic
from brigade import Brigade
from geographLocation import GeographLocation
from vars import *


def main():
    e = Employees()
    s = Shift()
    '''
    e.insert(
        "1",
        "kardanov",
        "islam",
        "ibragimovich",
        "M",
        "12.34.45",
        "89980909"
    )
    '''

    
    
    
    print(s.select_all_records())
    print(e.select_all_records())


    print("successful!")
    



if __name__ == "__main__":
    main()