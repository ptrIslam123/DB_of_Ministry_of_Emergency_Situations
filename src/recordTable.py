#! /usr/bin/env python
#-*-coding: utf-8-*-



import sqliteDriver as sql
from vars import *


class RecordTable:

    def __init__(self):
        self.__table_name = "Record"

        self.__sqlDriver = sql.SqlDriver(
           MAIN_SQL_DB_FILE
        )

        self.__sqlDriver.exec_request(
            "PRAGMA foreign_keys=on;"
        )

        self.__sqlDriver.exec_file(
            "{SQL_TABLES_DIR_PATH}/{__table_name}.txt".format(
                SQL_TABLES_DIR_PATH=SQL_TABLES_DIR_PATH,
                __table_name=self.__table_name
            )
        )



    def get_table_name(self):
        return self.__table_name


    def commit(self):
        self.__sqlDriver.commit()


    def print_table(self):
        self.__sqlDriver.exec_request(
            """
            SELECT sql FROM sqlite_master WHERE name='{__table_name}'
            """.format(__table_name=self.__table_name)
        )

        schema = self.__sqlDriver.fetchone()

        for i in schema:
            print(i)


    def insert(
        self,
        date,
        time,
        district_departue,
        address,
        visit_type,
        additional_data,
        sender_technics,
        rank,
        message
    ):
        '''
        CREATE TABLE IF NOT EXISTS Record
        (
            date                TEXT,                               -- дата
            time                TEXT,                               -- время
            district_departue   TEXT,                               -- район выезда
            address             TEXT,                               -- адресс выезда
            visit_type          TEXT,                               -- вид выезда
            additional_data     TEXT,                               -- дополнительные сведения
            sender_technics     TEXT,                               -- высылаемая техника
            rank                UNSIGNED INTEGER,                   -- уровень опасности
            message             TEXT,                               -- сообщение диспетчера

            CONSTRAINT pk_record PRIMARY KEY(date, time)
        );
        '''

        req = """
            INSERT INTO {__table_name}
            (date, time, district_departue, address, visit_type, additional_data, sender_technics, rank, message)
            VALUES
            (
                '{date}',
                '{time}',
                '{district_departue}',
                '{address}',
                '{visit_type}',
                '{additional_data}',
                '{sender_technics}',
                '{rank}',
                '{message}'
            );
        """.format(
            __table_name=self.__table_name,
            date=date,
            time=time,
            district_departue=district_departue,
            address=address,
            visit_type=visit_type,
            additional_data=additional_data,
            sender_technics=sender_technics,
            rank=rank,
            message=message
        )

        self.__sqlDriver.exec_request(
            req
        )


    def remove_records_by_date_and_time(self, date, time):
        req = """
            DELETE FROM {__table_name}
            WHERE date='{date}' AND time='{time}';
        """.format(
            __table_name=self.__table_name,
            date=date,
            time=time
        )

        self.__sqlDriver.exec_request(
            req
        )


    def update_records_by_date_and_time(
        self,
        search_data,
        search_time,
        date,
        time,
        district_departue,
        address,
        visit_type,
        additional_data,
        sender_technics,
        rank,
        message
    ):
        req = """
            UPDATE {__table_name}
            SET 
                date='{date}',
                time='{time}',
                district_departue='{district_departue}',
                address='{address}',
                visit_type='{visit_type}',
                additional_data='{additional_data}',
                sender_technics='{sender_technics}',
                rank='{rank}',
                message='{message}'
            
            WHERE date='{search_data}' AND time='{search_time}';
        """.format(
            __table_name=self.__table_name,
            search_data=search_data,
            search_time=search_time,
            date=date,
            time=time,
            district_departue=district_departue,
            address=address,
            visit_type=visit_type,
            additional_data=additional_data,
            sender_technics=sender_technics,
            rank=rank,
            message=message
        )

        self.__sqlDriver.exec_request(
            req
        )


    def find_records_by_date_and_time(self, date, time):
        req = """
            SELECT *
            FROM {__table_name}
            WHERE date='{date}' AND time='{time}'
        """.format(
            __table_name=self.__table_name,
            date=date,
            time=time
        )

        self.__sqlDriver.exec_request(
            req
        )

        return self.__sqlDriver.fetchall()



    def find_records_by_district_departue_and_address(self, district_departue, address):
        req = """
            SELECT *
            FROM {__table_name}
            WHERE district_departue='{district_departue}' AND address='{address}'
        """.format(
            __table_name=self.__table_name,
            district_departue=district_departue,
            address=address
        )

        self.__sqlDriver.exec_request(
            req
        )

        return self.__sqlDriver.fetchall()



    def select_all_records(self):
        self.__sqlDriver.exec_request(
            """
            SELECT *
            FROM {__table_name};
            """.format(__table_name=self.__table_name)
        )

        return self.__sqlDriver.fetchall()
