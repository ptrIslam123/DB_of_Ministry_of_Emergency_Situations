#! /usr/bin/env python
#-*-coding: utf-8-*-

from PySide import QtGui, QtCore
from widgetNames import *
import sys

from createWindow import *
from editWindow import *


class MainWindow(QtGui.QMainWindow):

    def __init__(self, titile, pos_x, pos_y, \
                width=DEFAULT_M_WINDOW_WIDTH, hight=DEFAULT_M_WINDOW_HIGHT):
        super(MainWindow, self).__init__()

        self.__title = titile
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__width = width
        self.__hight = hight

        
        self.__findWindow           = None
        self.__createWindow         = None
        self.__editWindow           = None

        
        self.initUI()
        self.createMenu()


    def initUI(self):
        self.setGeometry(
            self.__pos_x, 
            self.__pos_y, 
            self.__width, 
            self.__hight
        )

        self.setWindowTitle(self.__title)



    def createMenu(self):
        self.__action_open_file     = QtGui.QAction(MENU_FIELD_OPEN_FILE, self)
        self.__action_close_file    = QtGui.QAction(MENU_FIELD_CLOSE_FILE, self)
        self.__action_save_file     = QtGui.QAction(MENU_FIELD_SAVE_AS_FILE, self)
        
        self.__action_close_app     = QtGui.QAction(MENU_FIELD_EXIT_APP, self)
        
        self.__action_edit_record   = QtGui.QAction(MENU_FIELD_EDIT_RECORD, self)
        self.__action_create_record = QtGui.QAction(MENU_FIELD_CREATE_RECORD, self)
        
        self.__action_set_font      = QtGui.QAction(MENU_FIELD_EDIT_FONT, self)

        self.__action_find_records  = QtGui.QAction(MENU_FIELD_FIND_RECORDS, self)



        self.__action_open_file.triggered.connect(self.__open_file)
        self.__action_close_file.triggered.connect(self.__close_file)
        self.__action_save_file.triggered.connect(self.__save_file)
        self.__action_close_app.triggered.connect(self.close_window)
        self.__action_edit_record.triggered.connect(self.__edit_file)
        self.__action_create_record.triggered.connect(self.__create_file)
        self.__action_set_font.triggered.connect(self.__set_font)
        self.__action_find_records.triggered.connect(self.__find_records)


        self.__menubar              = self.menuBar()



        self.__file                 = self.__menubar.addMenu(MENU_FIELD_ACTION_FILE) 
        self.__edit                 = self.__menubar.addMenu(MENU_FIELD_ACTION_EDIT)
        self.__view                 = self.__menubar.addMenu(MENU_FIELD_ACTION_VIEW)
        self.__create               = self.__menubar.addMenu(MENU_FIELD_ACTION_CREATE)
        self.__find                 = self.__menubar.addMenu(MENU_FIELD_ACTION_FIND)



        self.__file.addAction(self.__action_open_file)
        self.__file.addAction(self.__action_save_file)
        self.__file.addAction(self.__action_close_file)
        self.__file.addAction(self.__action_close_app)

        self.__edit.addAction(self.__action_edit_record)

        self.__create.addAction(self.__action_create_record)

        self.__view.addAction(self.__action_set_font)

        self.__find.addAction(self.__action_find_records)

    
    def __open_file(self):
        print("open file!")

    def __close_file(self):
        print("close file!")

    def __save_file(self):
        print("save file!")

    def __edit_file(self):
        print("edit file!")
        if self.__editWindow is None:
            self.__editWindow = EditWindow()
        
        self.__editWindow.show_window()

    def __create_file(self):
        print("creaet file!")
        if self.__createWindow is None:
            self.__createWindow = CreateWindow()
        
        self.__createWindow.show_window()

    def __edit_font(self):
        print("edit font!")


    def __find_records(self):
        print("find records!")

    def __set_font(self):
        font, ok = QtGui.QFontDialog.getFont()

        if ok:
            pass
            #self.__textEdit.setFont(font)


    def close_window(self):
        QtCore.QCoreApplication.instance().quit()

    def show_window(self):
        self.show()

    
    


       


def main():
    app = QtGui.QApplication(sys.argv)
    
    mainW = MainWindow(
        MAIN_WINDOW_TITLE, 
        DEFAULT_M_WINDOW_POS_Y,
        DEFAULT_M_WINDOW_POS_X
    )

    mainW.show_window() 
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()