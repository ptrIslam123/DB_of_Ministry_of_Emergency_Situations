#! /usr/bin/env python
#-*-coding: utf-8-*-

import datetime


class Record:

    def __init__(self):
        self.__date                 = None
        self.__time                 = None
        self.__district_departue    = None
        self.__address              = None

        self.__entrance             = None
        self.__flat                 = None
        self.__floor                = None
        self.__phone_number         = None
        self.__reported             = None

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


    def get_str_record(self):
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
            __entrance={__entrance}\n
            __flat={__flat}\n
            __floor={__floor}\n
            __phone_number={__phone_number}\n
            __reported={__reported}\n
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
                __entrance=self.__entrance,
                __flat=self.__flat,
                __floor=self.__floor,
                __phone_number=self.__phone_number,
                __reported=self.__reported,
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


    def get__entrance(self):
        return self.__entrance

    
    def get_flat(self):
        return self.__flat


    def get_floor(self):
        return self.__floor


    def get_phone_number(self):
        return self.__phone_number


    def get_reported(self):
        return self.__reported


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

    def set_date(self, date):
        self.__date = date


    def set_time(self, time):
        self.__time = time


    def get_cur_date_str(self):
        return "{:%m.%d.%Y}".format(datetime.datetime.now().date())

    
    def get_cur_time_str(self):
        return "{:%H:%M}".format(datetime.datetime.now().time())


    def set_district_departue(self, val):
        self.__district_departue = val.encode('utf-8')


    def set_address(self, val):
        self.__address = val.encode('utf-8')


    def set_entrance(self, entrance):
        self.__entrance = entrance.encode('utf-8')


    def set_flat(self, flat):
        self.__flat = flat.encode('utf-8')


    def set_floor(self, floor):
        self.__floor = floor.encode('utf-8')


    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number.encode('utf-8')


    def set_reported(self, reported):
        self.__reported = reported.encode('utf-8')


    def set_visit_type(self, val):
        self.__visit_type = val.encode('utf-8')


    def set_additional_data(self, val):
        self.__additional_data = val.encode('utf-8')


    def set_sender_technics(self, val):
        self.__sender_technics = val.encode('utf-8')


    def set_rank(self, val):
        self.__rank = val.encode('utf-8')


    def set_message(self, val):
        self.__message = val.encode('utf-8')
        