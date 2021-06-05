#! /usr/bin/env python
#-*-coding: utf-8-*-

from recordTable import RecordTable 


class DBDriver:

    def __init__(self):
        self.__recordT = RecordTable()


    def write_new_record(self, record):
        # processing sql request error
        self.__recordT.insert(
            record.get_date(),
            record.get_time(),
            record.get_district_depatrue(),
            record.get_address(),
            record.get_visit_type(),
            record.get_additional_data(),
            record.get_sender_technics(),
            record.get_rank(),
            record.get_message()
        )

        return 0, self.__recordT.get_table_name()


    def edit_records(self):
        pass

        