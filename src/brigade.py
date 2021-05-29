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

    
    def commit(self):
        self.__sqlDriver.commit()


    def print_table(self):
        self.__sqlDriver.exec_request(
            """
            SELECT sql FROM sqlite_master WHERE name='Brigade'
            """
        )

        schema = self.__sqlDriver.fetchone()

        for i in schema:
            print(i)


    def insert(
        self,
        id_brigade,
        number_of_employyes,
        type_brigade
    ):
    
        '''
        CREATE TABLE IF NOT EXISTS Brigade
        (
            id_brigade              INTEGER,    -- Табельный номер бригады
            number_of_employyes     INTEGER,    -- Количество сотрудников
            type_brigade            TEXT,       -- Вид высылаемой бригады

            CONSTRAINT brigade_pk PRIMARY KEY(id_brigade)
        );
        '''

        req = """
            INSERT INTO Brigade
            (id_brigade, number_of_employyes, type_brigade)
            VALUES
            (
                '{id_brigade}',
                '{number_of_employyes}',
                '{type_brigade}'
            );
        """.format(
                id_brigade=id_brigade,
                number_of_employyes=number_of_employyes,
                type_brigade=type_brigade
        )       

        self.__sqlDriver.exec_request(
            req
        )

        self.__sqlDriver.commit()



    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM Brigade;
            """
        )

        return self.__sqlDriver.fetchall()