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
            record.get__entrance(),
            record.get_flat(),
            record.get_floor(),
            record.get_phone_number(),
            record.get_reported(),
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
        
        return 0, self.__recordT.get_table_name(), tuple_res


    def remove_records_by_date_and_time(self, date, time):
        # processing sql request error
        # 2021-06-05        : test data
        # 16:55:13.710367   : test data

        self.__recordT.remove_records_by_date_and_time(
            date, time
        )

        return 0, self.__recordT.get_table_name()


    def update_records_by_date_and_time(self, date, time, record):
        # processing sql request error
        # 2021-06-05
        # 16:56:29.839173

        self.__recordT.update_records_by_date_and_time(
            date, 
            time,
            record.get_district_depatrue(),
            record.get_address(),
            record.get_visit_type(),
            record.get_additional_data(),
            record.get_sender_technics(),
            record.get_rank(),
            record.get_message()
        )

        return 0, self.__recordT.get_table_name()



    def make_report_file_name(self, date, time):
        return "{date}{time}.rd".format(date=date, time=time)


    def tupleTostr(self, tuple_res):
        res = str("")

        for item in tuple_res:
            res += "{item}\n".format(item=str(item))

        return res