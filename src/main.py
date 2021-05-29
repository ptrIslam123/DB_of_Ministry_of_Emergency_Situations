#! /usr/bin/env python
#-*-coding: utf-8-*-


from sqliteDriver import *
from vars import *


def main():
    sql = SqlDriver("{SQL_TABLES_DIR_PATH}/Employees.db".format(
        SQL_TABLES_DIR_PATH=SQL_TABLES_DIR_PATH
    ))

    print("successful!")
    



if __name__ == "__main__":
    main()