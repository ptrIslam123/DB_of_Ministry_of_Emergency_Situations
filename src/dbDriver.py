#! /usr/bin/env python
#-*-coding: utf-8-*-


from recordTable import RecordTable 
from record import Record




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
        res_list = self.__recordT.find_records_by_date_and_time(
            date, time
        )

        return 0, self.__recordT.get_table_name(), self.listTostr(res_list).decode('utf-8')


    def remove_records_by_date_and_time(self, date, time):
        # processing sql request error

        self.__recordT.remove_records_by_date_and_time(
            date, time
        )

        return 0, self.__recordT.get_table_name()


    def update_records_by_date_and_time(self, list_data):
        # processing sql request error

        self.__recordT.update_records_by_date_and_time(
            list_data[0],
            list_data[1],
            list_data[2],
            list_data[3],
            list_data[4],
            list_data[5],
            list_data[6],
            list_data[7],
            list_data[8],
            list_data[9],
            list_data[10],
            list_data[11],
            list_data[12],
            list_data[13],
            list_data[14],
            list_data[15]
        )

        return 0, self.__recordT.get_table_name()


    def strRecordToListStrData(self, strRecord):
        list_data = strRecord.split("\n")
        list_data.pop(0)

        return list_data

        
            

    def get_all_records_into_table(self):
        return self.listTostr(
            self.__recordT.select_all_records()
        ).decode('utf-8')


    def make_report_file_name(self, date, time):
        return "{date}{time}.rd".format(date=date, time=time)


    def tupleTostr(self, tuple_res):
        res = str("")

        for item in tuple_res:
            res += "{item}\n".format(item=str(item))

        return res

    def listTostr(self, list_data):
        res_str = str()
        for i in list_data:
            for j in i:
                j = j.encode('utf-8')
                res_str = "{str1}\n{str2}".format(str1=res_str, str2=j)
        
        return res_str