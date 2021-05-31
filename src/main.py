#! /usr/bin/env python
#-*-coding: utf-8-*-


from employees import Employees 
from shift import Shift 
from technic import Technic  
from brigade import Brigade 
from geographLocation import GeographLocation 
from vars import *

from sqliteDriver import *

def main():
    e = Employees()
    s = Shift()
    
    e.insert(
        "1",
        "Kardanov",
        "Islam",
        "Ibragimovich",
        "M",
        "21.09.99",
        "89909090"
    )

    s.insert(
        "10",
        "1",
        "event1",
        "type1"
    )
    

    print(e.select_all_records())
    print(s.select_all_records())

    print("successful!")
    



if __name__ == "__main__":
    main()