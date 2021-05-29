#! /usr/bin/env python
#-*-coding: utf-8-*-


import sqliteDriver as sql
from vars import *

class Brigade:
    
    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/Brigade.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )

        self.__sqlDriver.exec_file(
            "{SQL_TABLES_DIR_PATH}/Brigade.txt".format(
                SQL_TABLES_DIR_PATH=SQL_TABLES_DIR_PATH
            )
        )