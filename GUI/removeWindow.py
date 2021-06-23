#! /usr/bin/env python
#-*-coding: utf-8-*-


from widgetAttribute import *
from window import *
import sys
import os

sys.path.append('../src/')
from record import Record
from dbDriver import DBDriver
import errorHandler
import vars
import loger


sys.path.append('../netAPI/')
from clientDB import TCPClinet, make_TCPClient
from netVars import *
from package import *



class RemoveRecordsWindow(BaseWindow):

    def __init__(self):
        super(RemoveRecordsWindow, self).__init__(
            REMOVE_WINDOW_TITLE,
            DEFAULT_RWINDOW_POS_X,
            DEFAULT_RWINDOW_POS_Y,
            DEFAULT_RWINDOW_WIDTH,
            DEFAULT_RWINDOW_HIGHT
        )

        self.__dbDriver             = DBDriver()
        self.__errHandler           = errorHandler.ErrorHandler()

        self.makeWindowDialog()


    def makeWindowDialog(self):
        self.__gridBox  = QtGui.QGridLayout()


        self.__remove_r_by_date_adn_time_btn    = QtGui.QPushButton(RWINDOW_REMOVE_BAUTTON)
        self.__cancel_btn                       = QtGui.QPushButton(CANCLE_BTN_NAME)


        self.__date_lbl                     = QtGui.QLabel(RWINDOW_DATE_LABEL)
        self.__time_lbl                     = QtGui.QLabel(RWINDOW_TIME_LABEL)

        self.__date_ledit                   = QtGui.QLineEdit()
        self.__time_ledit                   = QtGui.QLineEdit()
        self.__status_inf_ledit             = QtGui.QLineEdit()



        
        self.__gridBox.addWidget(self.__date_lbl, 1, 1)
        self.__gridBox.addWidget(self.__time_lbl, 2, 1)
        self.__gridBox.addWidget(self.__date_ledit, 1, 2)
        self.__gridBox.addWidget(self.__time_ledit, 2, 2)

        
        self.__gridBox.addWidget(self.__status_inf_ledit, 3, 1)
        self.__gridBox.addWidget(self.__remove_r_by_date_adn_time_btn, 3, 2)
        self.__gridBox.addWidget(self.__cancel_btn, 3, 3)



        self.setLayout(self.__gridBox)


        self.__remove_r_by_date_adn_time_btn.clicked.connect(self.__remove_r_by_date_and_time)
        self.__cancel_btn.clicked.connect(self.__clean_and_close_window)


    def __remove_r_by_date_and_time(self):
        date = self.__date_ledit.text()
        time = self.__time_ledit.text()

        res, table_name = self.__remove_record_on_server(date, time)

        if res != 0:
            self.__status_inf_ledit.setText(
                    self.__errHandler.handle(res, table_name)
            )

        else:
            res = self.__remove_report_file(
                self.__dbDriver.make_report_file_name(date, time)
            )
            if res != 0:
                self.__status_inf_ledit.setText(
                    self.__errHandler.handle(res, "Remove repoprt file fail")
                )
                
            else:
                self.__status_inf_ledit.setText(SUCCESSFULLY)
                loger.sys_write_log(vars.EVENT_LOG_TYPE, vars.SEARCH_DATA_INTO_THE_TABLE + table_name)
                #self.close_window()


    def __remove_record_on_server(self, date, time):
        client = make_TCPClient()

        if client.connect() != 0:
            pass

        package = Package(
            REMOVE_RECORD_PACKAGE_METHOD_TYPE,
            "{date}\n{time}".format(date=date, time=time)   
        )
        
        client.send_package(package)
        res_pkg, res = client.recive_package()

        if res != 0:
            return res_pkg.get_method_type(), self.get_table_name()

        else:
            client.destroy_connect()
            return 0, self.get_table_name()


    def __clean_and_close_window(self):
        self.__date_ledit.setText("")
        self.__time_ledit.setText("")
        self.__status_inf_ledit.setText("")

        self.close_window()


    def __remove_report_file(self, fname):
        file = "{path}/{fname}".format(path=vars.PATH_REPORTS_DIR, fname=fname)

        if os.path.exists(file) == False:
            return errorHandler.ERROR_REPOPT_FILE_NOT_FOUND    
        
        os.remove(file)
        return 0


    
