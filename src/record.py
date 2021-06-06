#! /usr/bin/env python
#-*-coding: utf-8-*-

from datetime import datetime


class Record:

    def __init__(self):
        self.__date                 = None
        self.__time                 = None
        self.__district_departue    = None
        self.__address              = None
        self.__visit_type           = None
        self.__additional_data      = None
        self.__sender_technics      = None
        self.__rank                 = None
        self.__message              = None



    def write_in_the_file(self, fname):
        with open(fname, 'w') as file:
            file.write("{__date}\n".format(__date=self.__date))
            file.write("{__time}\n".format(__time=self.__time))
            file.write("{__district_departue}\n".format(__district_departue=self.__district_departue))
            file.write("{__address}\n".format(__address=self.__address))
            file.write("{__visit_type}\n".format(__visit_type=self.__visit_type))
            file.write("{__additional_data}\n".format(__additional_data=self.__additional_data))
            file.write("{__sender_technics}\n".format(__sender_technics=self.__sender_technics))
            file.write("{__rank}\n".format(__rank=self.__rank))
            file.write("{__message}\n".format(__message=self.__message))


    def __get_str_record(self):
        reportData = """
        {__date}
        {__time}
        {__district_departue}
        {__address}
        {__visit_type}
        {__additional_data}
        {__sender_technics}
        {__rank}
        {__message}""".format(
            __date=self.__date,
            __time=self.__time,
            __district_departue=self.__district_departue,
            __address=self.__address,
            __visit_type=self.__visit_type,
            __additional_data=self.__additional_data,
            __sender_technics=self.__sender_technics,
            __rank=self.__rank,
            __message=self.__message
        )

        return reportData


    def print_fields(self):
        print(
            """
            __date={__date}\n
            __time={__time}\n
            __district_departue={__district_departue}\n
            __address={__address}\n
            __visit_type={__visit_type}\n
            __additional_data={__additional_data}\n
            __sender_technics={__sender_technics}\n
            __rank={__rank}\n
            __message={__message}\n
            """.format(
                __date=self.__date,
                __time=self.__time,
                __district_departue=self.__district_departue,
                __address=self.__address,
                __visit_type=self.__visit_type,
                __additional_data=self.__additional_data,
                __sender_technics=self.__sender_technics,
                __rank=self.__rank,
                __message=self.__message
        ))

    def get_date(self):
        return self.__date


    def get_time(self):
        return self.__time


    def get_district_depatrue(self):
        return self.__district_departue


    def get_address(self):
        return self.__address


    def get_visit_type(self):
        return self.__visit_type


    def get_additional_data(self):
        return self.__additional_data


    def get_sender_technics(self):
        return self.__sender_technics


    def get_rank(self):
        return self.__rank


    def get_message(self):
        return self.__message


    def set_cur_date(self):
        self.__date = datetime.now().date()

    
    def set_cur_time(self):
        hour    = datetime.now().time().hour
        minute  = datetime.now().time().minute

        self.__time = "{hour}:{minute}".format(hour=hour, minute=minute)


    def set_district_departue(self, val):
        self.__district_departue = val


    def set_address(self, val):
        self.__address = val


    def set_visit_type(self, val):
        self.__visit_type = val


    def set_additional_data(self, val):
        self.__additional_data = val


    def set_sender_technics(self, val):
        self.__sender_technics = val


    def set_rank(self, val):
        self.__rank = val


    def set_message(self, val):
        self.__message = val
        