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


    def find_records_by_date_and_time(self, date, time):
        # processing sql request error
        # 2021-06-05        : test data
        # 14:56:04.767042   : test data
        tuple_res = self.__recordT.find_records_by_date_and_time(
            date, time
        )[0]
        
        return 0, self.__recordT.get_table_name(), self.__tupleTostr(tuple_res)

        
    def __tupleTostr(self, tuple_res):
        res = str("")
        for item in tuple_res:
            res += "{item}\n".format(item=str(item))

        return res