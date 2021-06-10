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


class FindRecordsWindow(BaseWindow):

    def __init__(self):
        super(FindRecordsWindow, self).__init__(
            FIND_WINDOW_TITLE,
            DEFAULT_FWINDOW_POS_X,
            DEFAULT_FWINDOW_POS_Y,
            DEFAULT_FWINDOW_WIDTH,
            DEFAULT_FWINDOW_HIGHT
        )

        self.__dbDriver             = DBDriver()
        self.__errHandler           = errorHandler.ErrorHandler()

        self.makeWindowDialog()



    def makeWindowDialog(self):
        self.__gridBox  = QtGui.QGridLayout()


        self.__find_r_by_date_adn_time_btn  = QtGui.QPushButton(FWINDOW_FIND_BUTTON)
        self.__cancel_btn                   = QtGui.QPushButton(CANCLE_BTN_NAME)


        self.__date_lbl         = QtGui.QLabel(FWINDOW_DATE_LABEL)
        self.__time_lbl         = QtGui.QLabel(FWINDOW_TIME_LABEL)



        self.__date_ledit       = QtGui.QLineEdit()
        self.__time_ledit       = QtGui.QLineEdit()
        self.__status_inf_ledit = QtGui.QLineEdit()
        
        records_tedit_width     = 550
        records_tedit_higth     = 350
        self.__records_tedit    = QtGui.QTextEdit()
        self.__records_tedit.setFixedSize(records_tedit_width, records_tedit_higth)
        

        res_tedit_width         = records_tedit_width
        res_tedit_higth         = 150
        self.__res_tedit = QtGui.QTextEdit()
        self.__res_tedit.setFixedSize(res_tedit_width, res_tedit_higth)

        
        self.__gridBox.addWidget(self.__date_lbl, 1, 1)
        self.__gridBox.addWidget(self.__time_lbl, 2, 1)
        self.__gridBox.addWidget(self.__date_ledit, 1, 2)
        self.__gridBox.addWidget(self.__time_ledit, 2, 2)
        

        self.__gridBox.addWidget(self.__res_tedit, 4, 2)
        self.__gridBox.addWidget(self.__records_tedit, 5, 2)
        
        self.__gridBox.addWidget(self.__status_inf_ledit, 6, 2)
        self.__gridBox.addWidget(self.__find_r_by_date_adn_time_btn, 3, 3)
        self.__gridBox.addWidget(self.__cancel_btn, 6, 3)



        self.setLayout(self.__gridBox)


        self.__find_r_by_date_adn_time_btn.clicked.connect(self.__find_records_by_date_adn_time)
        self.__cancel_btn.clicked.connect(self.__clean_and_close_window)

        self.__write_all_records_in_the_textEdit()


    
    def __find_records_by_date_adn_time(self):
        
        date = self.__date_ledit.text()
        time = self.__time_ledit.text()

        res, table_name, data = self.__dbDriver.find_records_by_date_and_time(date, time)

        if res != 0:
            self.__status_inf_ledit.setText(
                    self.__errHandler.handle(res, table_name)
            )

        else:
            self.__status_inf_ledit.setText(SUCCESSFULLY)
            self.__res_tedit.setText(
                data
            )
            loger.write_log(vars.EVENT_LOG_TYPE, vars.SEARCH_DATA_INTO_THE_TABLE + table_name)



    def __write_all_records_in_the_textEdit(self):
        records = self.__dbDriver.get_all_records_into_table()
        self.__records_tedit.setText(records)


    def __clean_and_close_window(self):
        self.__date_ledit.setText("")
        self.__time_ledit.setText("")
        self.__status_inf_ledit.setText("")
        self.__res_tedit.setText("")

        self.close_window()

        

