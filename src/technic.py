#! /usr/bin/env python
#-*-coding: utf-8-*-


import sqliteDriver as sql
from vars import *

class Technic:

    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/Technic.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )

        self.__sqlDriver.exec_file(
            "{SQL_TABLES_DIR_PATH}/Technic.txt".format(
                SQL_TABLES_DIR_PATH=SQL_TABLES_DIR_PATH
            )
        )

    def commit(self):
        self.__sqlDriver.commit()


    def print_table(self):
        self.__sqlDriver.exec_request(
            """
            SELECT sql FROM sqlite_master WHERE name='Shift'
            """
        )

        schema = self.__sqlDriver.fetchone()

        for i in schema:
            print(i)


    def insert(
        self,
        id_car,
        gov_car_number,
        technic_type,
        last_name,
        firts_name,
        midle_name
    ):

        '''
        CREATE TABLE IF NOT EXISTS Technic
        (
            id_car              INTEGER,        -- Табельный номер ммашины
            gov_car_number      INTEGER,        -- Гос номер ммашины
            technic_type        TEXT,           -- Вид техники
            last_name           TEXT,           -- Фамилия водителя
            firts_name          TEXT,           -- Имя водителя
            midle_name          TEXT,           -- Отчество водителя

            CONSTRAINT technic_pk PRIMARY KEY(id_car),

            CONSTRAINT fk_l_name FOREIGN KEY (last_name) REFERENCES Employees(last_name),
            CONSTRAINT fk_f_name FOREIGN KEY (firts_name) REFERENCES Employees(firts_name),
            CONSTRAINT fk_m_name FOREIGN KEY (midle_name) REFERENCES Employees(midle_name)
        );
        '''

        req = """
            INSERT INTO Technic
            (id_car, gov_car_number, technic_type, last_name, firts_name, midle_name)
            VALUES
            (
                '{id_car}',
                '{gov_car_number}',
                '{technic_type}',
                '{last_name}',
                '{firts_name}',
                '{midle_name}'
            );
        """.format(
                id_car=id_car,
                gov_car_number=gov_car_number,
                technic_type=technic_type,
                last_name=last_name,
                firts_name=firts_name,
                midle_name=midle_name
        )

        self.__sqlDriver.exec_request(
            req
        )

        self.__sqlDriver.commit()



    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM Technic;
            """
        )

        return self.__sqlDriver.fetchall()