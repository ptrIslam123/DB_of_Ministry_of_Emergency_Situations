#! /usr/bin/env python
#-*-coding: utf-8-*-


from recordTable import RecordTable 
from vars import *

from sqliteDriver import *

def main():
    r = RecordTable()
    
    print(r.select_all_records())
    #r.print_table()
    '''
    r.insert(
        "12.12.12",
        "12:34",
        "Moscow",
        "address1",
        "entr1",
        "flat1",
        "floor1",
        "phone1",
        "person1",
        "visit_t1",
        "new data1",
        "technic1",
        "1",
        "message1"
    )
    '''

    print(r.select_all_records())
    print("successful!")
    



if __name__ == "__main__":
    main()