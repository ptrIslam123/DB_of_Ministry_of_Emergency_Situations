#! /usr/bin/env python
#-*-coding: utf-8-*-


from widgetAttribute import *
from window import *
import sys

sys.path.append('../src/')
from record import Record
from dbDriver import DBDriver
import errorHandler
import vars
import loger


class UpdateRecordsWindow(BaseWindow):

    def __init__(self):
        super(UpdateRecordsWindow, self).__init__(
            UPDATE_WINDOW_TITLE,
            DEFAULT_UWINDOW_POS_X,
            DEFAULT_UWINDOW_POS_Y,
            DEFAULT_UWINDOW_WIDTH,
            DEFAULT_UWINDOW_HIGHT
        )

        self.__dbDriver                 = DBDriver()
        self.__record                   = Record()
        self.__errorHandler             = errorHandler.ErrorHandler()

        self.__district_departue_list   = DISTRICT_DEPARTUE_LIST_VALUES
        self.__visit_type_list          = VISIT_TYPE_LIST_VALUES
        self.__additional_data_list     = ADDITIONAL_DATA_LIST_VALUES
        self.__sender_technics_list     = SENDER_TECHNIC_LIST_VALUES
        self.__rank_list                = RANK_LIST_VALUES

        self.__entered_date             = None
        self.__entered_time             = None

        self.makeWindowDialog()

    
    def makeWindowDialog(self):
        self.__gridBox  = QtGui.QGridLayout()

        self.__find_r_by_date_and_time_btn      = QtGui.QPushButton(UWINDOW_FIND_R_DATE_AND_TIME_BUTTON)
        self.__update_r_by_date_and_time_btn    = QtGui.QPushButton(UWINDOW_UPDATE_RECORD_BUTTON)
        self.__cancel_btn                       = QtGui.QPushButton(CANCLE_BTN_NAME)


        enter_date_lbl          = QtGui.QLabel(UWINDOW_FIND_R_BY_DATE_ADN_TIME)
        enter_time_lbl          = QtGui.QLabel(UWINDOW_FIND_R_BY_TIME_LABEL)
        status_inf_lbl          = QtGui.QLabel(UWINDOW_STATUS_INF_LABEL)
        district_departue_lbl   = QtGui.QLabel(UWINDOW_DISTRICT_DEPARTUE_LABEL)
        address_lbl             = QtGui.QLabel(UWINDOW_ADDRESS_LABEL)
        visit_type_lbl          = QtGui.QLabel(UWINDOW_VISIT_TYPE_LABEL)
        additional_data_lbl     = QtGui.QLabel(UWINDOW_ADDITIONAL_DATA_LABEL)
        sender_technics_lbl     = QtGui.QLabel(UWINDOW_SENDED_TECHNICS_LABEL)
        rank_lbl                = QtGui.QLabel(UWINDOW_RANK_LABEL)
        message_lbl             = QtGui.QLabel(UWINDOW_MESSAGE_LABEL)


        self.__enter_date_ledit             = QtGui.QLineEdit()
        self.__enter_time_ledit             = QtGui.QLineEdit()
        self.__status_inf_ledit             = QtGui.QLineEdit()
        self.__district_departue_ledit      = QtGui.QComboBox()
        self.__district_departue_ledit.addItems(
            self.__district_departue_list
        )
        self.__district_departue_ledit.activated[str].connect(self.__district_departue_handler)

        self.__address_ledit                = QtGui.QLineEdit()
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



        self.__gridBox.addWidget(enter_date_lbl, 1, 1)
        self.__gridBox.addWidget(enter_time_lbl, 2, 1)

        self.__gridBox.addWidget(self.__enter_date_ledit, 1, 2)
        self.__gridBox.addWidget(self.__enter_time_ledit, 2, 2)
        self.__gridBox.addWidget(self.__find_r_by_date_and_time_btn, 3, 4)


        self.__gridBox.addWidget(district_departue_lbl, 4, 1)
        self.__gridBox.addWidget(address_lbl, 5, 1)
        self.__gridBox.addWidget(visit_type_lbl, 6, 1)
        self.__gridBox.addWidget(additional_data_lbl, 7, 1)
        self.__gridBox.addWidget(sender_technics_lbl, 8, 1)
        self.__gridBox.addWidget(rank_lbl, 9, 1)
        self.__gridBox.addWidget(message_lbl, 10, 1)
        self.__gridBox.addWidget(status_inf_lbl, 11, 1)

        self.__gridBox.addWidget(self.__district_departue_ledit, 4, 2)
        self.__gridBox.addWidget(self.__address_ledit, 5, 2)
        self.__gridBox.addWidget(self.__visit_type_ledit, 6, 2)
        self.__gridBox.addWidget(self.__additional_data_ledit, 7,  2)
        self.__gridBox.addWidget(self.__sender_technics_ledit, 8, 2)
        self.__gridBox.addWidget(self.__rank_ledit, 9, 2)
        self.__gridBox.addWidget(self.__message_ledit, 10, 1)


        self.__gridBox.addWidget(self.__status_inf_ledit, 11, 2)
        self.__gridBox.addWidget(self.__update_r_by_date_and_time_btn, 11, 3)
        self.__gridBox.addWidget(self.__cancel_btn, 11, 4)


        self.setLayout(self.__gridBox)


        self.__find_r_by_date_and_time_btn.clicked.connect(self.__find_need_record_by_date_and_time)
        self.__update_r_by_date_and_time_btn.clicked.connect(self.__update_records_by_date_and_time)
        self.__cancel_btn.clicked.connect(self.close_window)



    def __update_records_by_date_and_time(self):
        
        self.__record.set_cur_date()
        self.__record.set_cur_time()
        self.__record.set_address(self.__address_ledit.text())
        self.__record.set_message(self.__message_ledit.toPlainText())

        res, table_name = self.__dbDriver.update_records_by_date_and_time(
            self.__entered_date, self.__entered_time ,self.__record
        )

        if res != 0:
            self.__status_inf_ledit.setText(
                self.__errorHandler.handle(res, table_name)
            )

        else:
            self.__status_inf_ledit.setText(SUCCESSFULLY)
            self.__update_report_file(self.__record)
            loger.write_log(vars.EVENT_LOG_TYPE, vars.INSERT_DATA_INTO_THE_TABLE + table_name)
            #self.close_window()


    def __find_need_record_by_date_and_time(self):
        self.__entered_date = self.__enter_date_ledit.text()
        self.__entered_time = self.__enter_time_ledit.text()

        res, table_name, tuple_records = self.__dbDriver.find_records_by_date_and_time(
            self.__entered_date, self.__entered_time
        )

        if res != 0:
            self.__status_inf_ledit.setText(
                    self.__errHandler.handle(res, table_name)
            )

        else:
            self.__set_old_values_for_fileds(tuple_records)
            self.__status_inf_ledit.setText(SUCCESSFULLY)
        

    def __clean_and_close_window(self):
        self.__enter_date_ledit.setText("")
        self.__enter_time_ledit.setText("")
        self.__status_inf_ledit.setText("")
        self.__address_ledit.setText("")
        self.__message_ledit.setText("")

        self.close_window()


    def __set_old_values_for_fileds(self, tuple_data):
        old_address_val = tuple_data[3] # 3
        old_message_val = tuple_data[8] # 8

        self.__address_ledit.setText(old_address_val)
        self.__message_ledit.setText(old_message_val)


    def __update_report_file(self, record):
        pass


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


    
