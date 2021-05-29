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
    #id_employees,
    #last_name,
    #firts_name,
    #midle_name,
    #gender,
    #date_of_burth,
    #number_phone

    #e.print_table()
    e.insert(
        "1",
        "kardanov",
        "islam",
        "ibrag",
        "M",
        "12.34.45",
        "89980909"
    )

    e.insert(
        "2",
        "fff1",
        "fff2",
        "fff3",
        "M",
        "12.34.45",
        "89980909"
    )
    

    print(e.select_all_records())


    print("successful!")
    



if __name__ == "__main__":
    main()