#! /usr/bin/env python
#-*-coding: utf-8-*-


from PySide import QtGui, QtCore


class BaseWindow(QtGui.QWidget, object):

    def __init__(self, titile, pos_x, pos_y, width=300, hight=300):
        super(BaseWindow, self).__init__()

        self.__title = titile
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__width = width
        self.__hight = hight

        self.initUI()


    def initUI(self):
        self.setGeometry(
            self.__pos_x, 
            self.__pos_y, 
            self.__width, 
            self.__hight
        )

        self.setWindowTitle(self.__title)


    def get_table_name(self):
        return "Record"


    def show_window(self):
        self.show()


    def close_window(self):
        self.close()