#! /usr/bin/env python
#-*-coding: utf-8-*-


from recordTable import RecordTable 
from dbDriver import DBDriver
from vars import *

from sqliteDriver import *

def main():
    r = RecordTable()
    r.insert(
        "date",
        "time",
        "district_departue",
        "address",
        "entrance",
        "flat",
        "floor",
        "phone_number",
        "reported",
        "visit_type",
        "additional_data",
        "sender_technics",
        "rank",
        "message"
    )

    db = DBDriver()
    #res = db.listTostr(r.select_all_records())
    #print("[\n{res}\n]".format(res=res))
    #print("successful!")
    



if __name__ == "__main__":
    main()