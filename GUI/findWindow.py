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


        self.__res_tedit = QtGui.QTextEdit()


        
        self.__gridBox.addWidget(self.__date_lbl, 1, 1)
        self.__gridBox.addWidget(self.__time_lbl, 2, 1)
        self.__gridBox.addWidget(self.__date_ledit, 1, 2)
        self.__gridBox.addWidget(self.__time_ledit, 2, 2)

        self.__gridBox.addWidget(self.__res_tedit, 3, 2)
        
        self.__gridBox.addWidget(self.__status_inf_ledit, 4, 1)
        self.__gridBox.addWidget(self.__find_r_by_date_adn_time_btn, 4, 2)
        self.__gridBox.addWidget(self.__cancel_btn, 4, 3)



        self.setLayout(self.__gridBox)


        self.__find_r_by_date_adn_time_btn.clicked.connect(self.__find_records_by_date_adn_time)
        self.__cancel_btn.clicked.connect(self.__clean_and_close_window)


    
    def __find_records_by_date_adn_time(self):
        date = self.__date_ledit.text()
        time = self.__time_ledit.text()

        res, table_name, tuple_records = self.__dbDriver.find_records_by_date_and_time(date, time)

        if res != 0:
            self.__status_inf_ledit.setText(
                    self.__errHandler.handle(res, table_name)
            )

        else:
            self.__status_inf_ledit.setText(SUCCESSFULLY)
            self.__res_tedit.setText(
                self.__dbDriver.tupleTostr(tuple_records)
            )
            loger.write_log(vars.EVENT_LOG_TYPE, vars.SEARCH_DATA_INTO_THE_TABLE + table_name)


    def __clean_and_close_window(self):
        self.__date_ledit.setText("")
        self.__time_ledit.setText("")
        self.__status_inf_ledit.setText("")
        self.__res_tedit.setText("")

        self.close_window()

        

