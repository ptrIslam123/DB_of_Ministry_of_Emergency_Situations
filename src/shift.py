#! /usr/bin/env python
#-*-coding: utf-8-*-



import sqliteDriver as sql
from vars import *

class Shift:
    
    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            "{SQL_DB_DIR_PATH}/Shift.db".format(
                SQL_DB_DIR_PATH=SQL_DB_DIR_PATH
            )
        )

        self.__sqlDriver.exec_file(
            "{SQL_TABLES_DIR_PATH}/Shift.txt".format(
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
        id_shift,
        event_type,
        last_name,
        firts_name,
        midle_name,
        visit_type
    ):
    
        '''
        CREATE TABLE IF NOT EXISTS Shift
        (
            id_shift            INTEGER,        -- Номер смены
            event_type          TEXT,           -- Тип события (проишествия)
            last_name           TEXT,           -- Фамилия дежурного
            firts_name          TEXT,           -- Имя дежурного
            midle_name          TEXT,           -- Отчество дежурного
            visit_type          TEXT,           -- Вид выезда

            CONSTRAINT shift_pk PRIMARY KEY(id_shift),

            CONSTRAINT fk_l_name FOREIGN KEY (last_name) REFERENCES Employees(last_name),
            CONSTRAINT fk_f_name FOREIGN KEY (firts_name) REFERENCES Employees(firts_name),
            CONSTRAINT fk_m_name FOREIGN KEY (midle_name) REFERENCES Employees(midle_name)
        );
        '''

        req = """
            INSERT INTO Shift
            (id_shift, event_type, last_name, firts_name, midle_name, visit_type)
            VALUES
            (
                '{id_shift}',
                '{event_type}',
                '{last_name}',
                '{firts_name}',
                '{midle_name}',
                '{visit_type}'
            );
        """.format(
                id_shift=id_shift,
                event_type=event_type,
                last_name=last_name,
                firts_name=firts_name,
                midle_name=midle_name,
                visit_type=visit_type
        )       

        self.__sqlDriver.exec_request(
            req
        )

        self.__sqlDriver.commit()



    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM Shift;
            """
        )

        return self.__sqlDriver.fetchall()