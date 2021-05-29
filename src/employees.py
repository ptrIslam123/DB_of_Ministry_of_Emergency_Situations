#! /usr/bin/env python
#-*-coding: utf-8-*-


import sqliteDriver as sql
from vars import *

class Employees:
    
    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/Employees.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )

        self.__sqlDriver.exec_file(
            "{SQL_TABLES_DIR_PATH}/Employees.txt".format(
                SQL_TABLES_DIR_PATH=SQL_TABLES_DIR_PATH
            )
        )


    def commit(self):
        self.__sqlDriver.commit()


    def print_table(self):
        self.__sqlDriver.exec_request(
            """
            SELECT sql FROM sqlite_master WHERE name='Employees'
            """
        )

        schema = self.__sqlDriver.fetchone()

        for i in schema:
            print(i)



    def insert(
        self,
        id_employees,
        last_name,
        firts_name,
        midle_name,
        gender,
        date_of_burth,
        number_phone
    ):

        '''
        CREATE TABLE Employees
        (
            id_employees        INTEGER         -- табельный номер
            last_name           TEXT,           -- Фамилия
            firts_name          TEXT,           -- Имя
            midle_name          TEXT,           -- Отчество
            gender              TEXT,           -- Пол
            date_of_burth       TEXT,           -- Дата рождения
            number_phone        TEXT,           -- Номер телефона

            CONSTRAINT employyes_pk PRIMARY KEY(id_employees)
        )
        '''

        req = """
            INSERT INTO Employees
            (id_employees, last_name, firts_name, midle_name, gender, date_of_burth, number_phone)
            VALUES
            (
                '{id_employees}', 
                '{last_name}',
                '{firts_name}', 
                '{midle_name}', 
                '{gender}', 
                '{date_of_burth}', 
                '{number_phone}');
        """.format(
                id_employees=id_employees,
                last_name=last_name,
                firts_name=firts_name,
                midle_name=midle_name,
                gender=gender,
                date_of_burth=date_of_burth,
                number_phone=number_phone
        )

        self.__sqlDriver.exec_request(
                req
        )

        self.__sqlDriver.commit()



    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM Employees;
            """
        )

        return self.__sqlDriver.fetchall()
