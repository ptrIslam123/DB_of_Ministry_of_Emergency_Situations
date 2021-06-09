#! /usr/bin/env python
#-*-coding: utf-8-*-

from widgetAttribute import *
from window import *
import sys

sys.path.append('../src/')
from record import Record
from dbDriver import DBDriver
from errorHandler import ErrorHandler
import vars
import loger


class CreateRecordWindow(BaseWindow):

    def __init__(self):
        super(CreateRecordWindow, self).__init__(
            CREATE_WINDOW_TITLE,
            DEFAULT_CWINDOW_POS_X,
            DEFAULT_CWINDOW_POS_Y,
            DEFAULT_CWINDOW_WIDTH,
            DEFAULT_M_WINDOW_HIGHT
        )

        self.__dbDriver                 = DBDriver()
        self.__record                   = Record()
        self.__errorHandler             = ErrorHandler()

        self.__district_departue_list   = DISTRICT_DEPARTUE_LIST_VALUES
        self.__visit_type_list          = VISIT_TYPE_LIST_VALUES
        self.__additional_data_list     = ADDITIONAL_DATA_LIST_VALUES
        self.__sender_technics_list     = SENDER_TECHNIC_LIST_VALUES
        self.__rank_list                = RANK_LIST_VALUES

        self.makeWindowDialog()

    
        


    
    def makeWindowDialog(self):
        self.__gridBox  = QtGui.QGridLayout()

        self.__write_btn = QtGui.QPushButton(CWINDOW_WRITE_BTN_NAME)
        self.__cancel_btn = QtGui.QPushButton(CANCLE_BTN_NAME)


        
        date_lbl                = QtGui.QLabel(CWINDOW_DATE_LABEL)
        time_lbl                = QtGui.QLabel(CWINDOW_TIME_LABEL)

        entrance_lbl            = QtGui.QLabel(CWINDOW_ENTRANCE_LABEL)    # подъезд
        flat_lbl                = QtGui.QLabel(CWINDOW_FLAT_LABEL)    # квартира
        floor_lbl               = QtGui.QLabel(CWINDOW_FLOOR_LABEL)    # этаж
        phone_number_lbl        = QtGui.QLabel(CWINDOW_PHONE_NUMBER_LABEL)    # номер телефона
        reported_lbl            = QtGui.QLabel(CWINDOW_REPORTED_LABEL)    # сообщил (доложил)


        status_inf_lbl          = QtGui.QLabel(CWINDOW_STATUS_INF_LABEL)
        district_departue_lbl   = QtGui.QLabel(CWINDOW_DISTRICT_DEPARTUE_LABEL)
        address_lbl             = QtGui.QLabel(CWINDOW_ADDRESS_LABEL)
        visit_type_lbl          = QtGui.QLabel(CWINDOW_VISIT_TYPE_LABEL)
        additional_data_lbl     = QtGui.QLabel(CWINDOW_ADDITIONAL_DATA_LABEL)
        sender_technics_lbl     = QtGui.QLabel(CWINDOW_SENDED_TECHNICS_LABEL)
        rank_lbl                = QtGui.QLabel(CWINDOW_RANK_LABEL)
        message_lbl             = QtGui.QLabel(CWINDOW_MESSAGE_LABEL)


        self.__date_ledit                   = QtGui.QLineEdit()
        self.__time_ledit                   = QtGui.QLineEdit()


        self.__entrance_ledit               = QtGui.QLineEdit()
        self.__flat_ledit                   = QtGui.QLineEdit()
        self.__floor_ledit                  = QtGui.QLineEdit()
        self.__phone_number_ledit           = QtGui.QLineEdit()
        self.__reported_ledit               = QtGui.QLineEdit()


        self.__status_inf_ledit             = QtGui.QLineEdit()
        self.__district_departue_ledit      = QtGui.QComboBox()
        self.__district_departue_ledit.addItems(
            self.__district_departue_list
        )
        self.__district_departue_ledit.activated[str].connect(self.__district_departue_handler)

        self.__address_ledit                = QtGui.QLineEdit()


        self.__date_ledit.setText(self.__record.get_cur_date_str())
        self.__time_ledit.setText(self.__record.get_cur_time_str())


        self.__visit_type_ledit             = QtGui.QComboBox()
        self.__visit_type_ledit.addItems(
            self.__visit_type_list
        )
        self.__visit_type_ledit.activated[str].connect(self.__visit_type_handler)

        self.__additional_data_ledit        = QtGui.QComboBox()
        self.__additional_data_ledit.addItems(
            self.__additional_data_list
        )
        self.__additional_data_ledit.activated[str].connect(self.__additional_data_handler)

        self.__sender_technics_ledit        = QtGui.QComboBox()
        self.__sender_technics_ledit.addItems(
            self.__sender_technics_list
        )
        self.__sender_technics_ledit.activated[str].connect(self.__sender_technics_handler)

        self.__rank_ledit                   = QtGui.QComboBox()
        self.__rank_ledit.addItems(
            self.__rank_list
        )
        self.__rank_ledit.activated[str].connect(self.__rank_handler)

        self.__message_ledit                = QtGui.QTextEdit()



        self.__gridBox.addWidget(date_lbl, 1, 1)
        self.__gridBox.addWidget(time_lbl, 2, 1)
        self.__gridBox.addWidget(district_departue_lbl, 3, 1)
        self.__gridBox.addWidget(address_lbl, 4, 1)

        self.__gridBox.addWidget(entrance_lbl, 5, 1)
        self.__gridBox.addWidget(flat_lbl, 6, 1)
        self.__gridBox.addWidget(floor_lbl, 7, 1)
        self.__gridBox.addWidget(phone_number_lbl, 8, 1)
        self.__gridBox.addWidget(reported_lbl, 9, 1)

        self.__gridBox.addWidget(visit_type_lbl, 10, 1)
        self.__gridBox.addWidget(additional_data_lbl, 11, 1)
        self.__gridBox.addWidget(sender_technics_lbl, 12, 1)
        self.__gridBox.addWidget(rank_lbl, 13, 1)
        self.__gridBox.addWidget(message_lbl, 14, 1)
        self.__gridBox.addWidget(status_inf_lbl, 15, 1)



        self.__gridBox.addWidget(self.__date_ledit, 1, 2)
        self.__gridBox.addWidget(self.__time_ledit, 2, 2)
        self.__gridBox.addWidget(self.__district_departue_ledit, 3, 2)
        self.__gridBox.addWidget(self.__address_ledit, 4, 2)

        self.__gridBox.addWidget(self.__entrance_ledit, 5, 2)
        self.__gridBox.addWidget(self.__flat_ledit, 6, 2)
        self.__gridBox.addWidget(self.__floor_ledit, 7, 2)
        self.__gridBox.addWidget(self.__phone_number_ledit, 8, 2)
        self.__gridBox.addWidget(self.__reported_ledit, 9, 2)


        self.__gridBox.addWidget(self.__visit_type_ledit, 10, 2)
        self.__gridBox.addWidget(self.__additional_data_ledit, 11,  2)
        self.__gridBox.addWidget(self.__sender_technics_ledit, 12, 2)
        self.__gridBox.addWidget(self.__rank_ledit, 13, 2)
        self.__gridBox.addWidget(self.__message_ledit, 14, 1)


        self.__gridBox.addWidget(self.__status_inf_ledit, 15, 2)
        self.__gridBox.addWidget(self.__write_btn, 15, 3)
        self.__gridBox.addWidget(self.__cancel_btn, 15, 4)


        self.setLayout(self.__gridBox)

        self.__write_btn.clicked.connect(self.write_record_in_the_db)
        self.__cancel_btn.clicked.connect(self.__clean_and_close_window)



    def write_record_in_the_db(self):

        self.__record.set_date(self.__date_ledit.text())
        self.__record.set_time(self.__date_ledit.text())

        self.__record.set__entrance(self.__entrance_ledit.text())
        self.__record.set_flat(self.__flat_ledit.text())
        self.__record.set_floor(self.__floor_ledit.text())
        self.__record.set_phone_number(self.__phone_number_ledit.text())
        self.__record.set_reported(self.__reported_ledit.text())
        
        self.__record.set_address(self.__address_ledit.text())
        self.__record.set_message(self.__message_ledit.toPlainText())

        self.__record.print_fields()

        res, table_name = self.__dbDriver.write_new_record(self.__record)

        if res != 0:
            self.__status_inf_ledit.setText(
                self.__errorHandler.handle(res, table_name)
            )

        else:
            self.__status_inf_ledit.setText(SUCCESSFULLY)
            self.__make_report_file(self.__record)
            loger.write_log(vars.EVENT_LOG_TYPE, vars.INSERT_DATA_INTO_THE_TABLE + table_name)
            #self.close_window()
        
    
    def __clean_and_close_window(self):
        self.__status_inf_ledit.setText("")
        self.__address_ledit.setText("")
        self.__message_ledit.setText("")

        self.close_window()


    def __make_report_file(self, record):
        filePath = "{PATH_REPORTS_DIR}/{date}{time}.rd".format(
                PATH_REPORTS_DIR=vars.PATH_REPORTS_DIR,
                date=record.get_date(),
                time=record.get_time()
        )    
        
        record.write_in_the_file(filePath)




    def __district_departue_handler(self, text):
        self.__record.set_district_departue(text)


    def __visit_type_handler(self, text):
        self.__record.set_visit_type(text)


    def __additional_data_handler(self, text):
        self.__record.set_additional_data(text)


    def __sender_technics_handler(self, text):
        self.__record.set_sender_technics(text)


    def __rank_handler(self, text):
        self.__record.set_rank(text)


    
