#! /usr/bin/env python
#-*-coding: utf-8-*-


from recordTable import RecordTable 
from dbDriver import DBDriver
from vars import *

from sqliteDriver import *






def main():
    r = RecordTable()
   
    
    db = DBDriver()
    res = db.listTostr(r.select_all_records())
    print("[\n{res}\n]".format(res=res))
    print("successful!")
    



if __name__ == "__main__":
    main()