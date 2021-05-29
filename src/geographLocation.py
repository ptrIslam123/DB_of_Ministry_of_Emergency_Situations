#! /usr/bin/env python
#-*-coding: utf-8-*-



import sqliteDriver as sql
from vars import *

class GeographLocation:
    
    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/GeographLocation.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )

        self.__sqlDriver.exec_file(
            "{SQL_TABLES_DIR_PATH}/GeographLocation.txt".format(
                SQL_TABLES_DIR_PATH=SQL_TABLES_DIR_PATH
            )
        )


    def commit(self):
        self.__sqlDriver.commit()


    def print_table(self):
        self.__sqlDriver.exec_request(
            """
            SELECT sql FROM sqlite_master WHERE name='GeographLocation'
            """
        )

        schema = self.__sqlDriver.fetchone()

        for i in schema:
            print(i)


    def insert(
        self,
        district_number,
        address,
        visit_type,
        description
    ):
    
        '''
        CREATE TABLE IF NOT EXISTS GeographLocation
        ( 
            district_number     INTEGER,    -- Номер района
            address             TEXT,       -- Адрес
            visit_type          TEXT,       -- Вид выезда
            description         TEXT,       -- Дополнительные сведения

            CONSTRAINT geographLocation_pk PRIMARY KEY(district_number)
        ); 
        '''

        req = """
            INSERT INTO GeographLocation
            (district_number, address, visit_type, description)
            VALUES
            (
                '{district_number}',
                '{address}',
                '{visit_type}',
                '{description}'
            );
        """.format(
                district_number=district_number,
                address=address,
                visit_type=visit_type,
                description=description
        )       

        self.__sqlDriver.exec_request(
            req
        )

        self.__sqlDriver.commit()



    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM GeographLocation;
            """
        )

        return self.__sqlDriver.fetchall()