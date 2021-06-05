#! /usr/bin/env python
#-*-coding: utf-8-*-


from employees import Employees 
from shift import Shift 
from technic import Technic  
from brigade import Brigade 
from geographLocation import GeographLocation
from recordTable import Record 
from vars import *

from sqliteDriver import *

def main():
    r = Record()
    
    r.insert(
        "12.12.12",
        "12:34",
        "Moscow",
        "address1",
        "visit_t1",
        "new data1",
        "technic1",
        "1",
        "message1"
    )

    r.insert(
        "12.10.12",
        "12:35",
        "Moscow",
        "address2",
        "visit_t2",
        "new data2",
        "technic2",
        "2",
        "message2"
    )

    print(r.select_all_records())
    print("-------- find_records_by_date_and_time ---------------\n")
    print(r.find_records_by_date_and_time(
        "12.10.12", "12:35"
    ))
    print("-------- remove_records_by_date_and_time ---------------\n")
    r.remove_records_by_date_and_time(
        "12.10.12","12:35"
    )
    print(r.select_all_records())
    print("successful!")
    



if __name__ == "__main__":
    main()