#! /usr/bin/env python
#-*-coding: utf-8-*-



import sqliteDriver as sql
from vars import *

class Shift:
    
    def __init__(self):
        self.__sqlDriver = sql.SqlDriver(
            MAIN_SQL_DB_FILE
        )


        self.__sqlDriver.exec_request(
            "PRAGMA foreign_keys=on;"
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
        id_employees,
        event_type,
        visit_type
    ):
    
        '''
        CREATE TABLE IF NOT EXISTS Shift
        (
            id_shift            INTEGER,        -- Номер смены
            id_employees        INTEGER,        -- идентивикатор сотрудника (является внешним ключом по отношений к таблице Employees)
            event_type          TEXT,           -- Тип события (проишествия)
            visit_type          TEXT,           -- Вид выезда

            CONSTRAINT pk_shift PRIMARY KEY(id_shift),

            CONSTRAINT fk_id_employees FOREIGN KEY(id_employees) REFERENCES Employees(id_employees)
        );
        '''

        req = """
            INSERT INTO Shift
            (id_shift, id_employees, event_type, visit_type)
            VALUES
            (
                '{id_shift}',
                '{id_employees}',
                '{event_type}',
                '{visit_type}'
            );
        """.format(
                id_shift=id_shift,
                id_employees=id_employees,
                event_type=event_type,
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