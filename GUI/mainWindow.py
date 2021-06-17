#! /usr/bin/env python
#-*-coding: utf-8-*-

from PySide import QtGui, QtCore
from widgetAttribute import *
import sys

from createWindow import *
from updateWindow import *
from findWindow import *
from removeWindow import *
from autorizationWindow import *


sys.path.append('../src/')
from autointoxication import Passwd, write_passwd_in_file, read_passwd_from_file




class MainWindow(QtGui.QMainWindow):

    def __init__(self, titile, pos_x, pos_y, \
                width=DEFAULT_M_WINDOW_WIDTH, hight=DEFAULT_M_WINDOW_HIGHT):
        super(MainWindow, self).__init__()

        self.__title = titile
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__width = width
        self.__hight = hight

        
        self.__findRecordsWindow            = None
        self.__createRecordsWindow          = None
        self.__updateRecordsWindow          = None
        self.__removeRecordsWindow          = None

        
        self.initUI()
        self.createMenu()


    def initUI(self):
        self.setGeometry(
            self.__pos_x, 
            self.__pos_y, 
            self.__width, 
            self.__hight
        )

        self.__textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.__textEdit)

        self.setWindowTitle(self.__title)



    def createMenu(self):
        self.__action_open_file     = QtGui.QAction(MENU_FIELD_OPEN_FILE, self)
        self.__action_close_file    = QtGui.QAction(MENU_FIELD_CLOSE_FILE, self)
        self.__action_save_file     = QtGui.QAction(MENU_FIELD_SAVE_AS_FILE, self)
        
        self.__action_close_app     = QtGui.QAction(MENU_FIELD_EXIT_APP, self)    
        self.__action_set_font      = QtGui.QAction(MENU_FIELD_EDIT_FONT, self)


        self.__action_find_records_by_date_and_time     = QtGui.QAction(CWINDOW_FIND_R_BY_DATE_ADN_TIME, self)
        self.__action_update_records_by_date_adn_time   = QtGui.QAction(CWINDOW_UPDATE_R_BY_DATE_AND_TIME, self)
        self.__action_remove_records_by_date_and_time   = QtGui.QAction(CWINDOW_REMOVE_R_BY_DATE_ADN_TIME, self) 
        self.__action_create_new_record                 = QtGui.QAction(MENU_FIELD_CREATE_RECORD, self)



        self.__action_open_file.triggered.connect(self.__open_file)
        self.__action_close_file.triggered.connect(self.__close_file)
        self.__action_save_file.triggered.connect(self.__save_file)
        self.__action_close_app.triggered.connect(self.close_window)
        self.__action_set_font.triggered.connect(self.__set_font)
        

        
        self.__action_create_new_record.triggered.connect(self.__create_new_records)
        self.__action_find_records_by_date_and_time.triggered.connect(self.__find_records_by_date_adn_time)
        self.__action_update_records_by_date_adn_time.triggered.connect(self.__update_records_by_date_and_time)
        self.__action_remove_records_by_date_and_time.triggered.connect(self.__remove_records_by_date_and_time)



        self.__menubar              = self.menuBar()



        self.__file                 = self.__menubar.addMenu(MENU_FIELD_ACTION_FILE) 
        self.__edit                 = self.__menubar.addMenu(MENU_FIELD_ACTION_EDIT)
        self.__view                 = self.__menubar.addMenu(MENU_FIELD_ACTION_VIEW)
        self.__create               = self.__menubar.addMenu(MENU_FIELD_ACTION_CREATE)
        self.__find                 = self.__menubar.addMenu(MENU_FIELD_ACTION_FIND)
        self.__remove               = self.__menubar.addMenu(MENU_FIELD_ACTION_REMOVE)



        self.__file.addAction(self.__action_open_file)
        self.__file.addAction(self.__action_save_file)
        self.__file.addAction(self.__action_close_file)
        self.__file.addAction(self.__action_close_app)
        self.__view.addAction(self.__action_set_font)


        self.__edit.addAction(self.__action_update_records_by_date_adn_time)
        self.__create.addAction(self.__action_create_new_record)
        self.__find.addAction(self.__action_find_records_by_date_and_time)
        self.__remove.addAction(self.__action_remove_records_by_date_and_time)

    
    


    def __update_records_by_date_and_time(self):
        self.__updateRecordsWindow = UpdateRecordsWindow()
        self.__updateRecordsWindow.show_window()


    def __create_new_records(self):
        self.__createRecordsWindow = CreateRecordWindow()
        self.__createRecordsWindow.show_window()


    def __find_records_by_date_adn_time(self):
        self.__findRecordsWindow = FindRecordsWindow()
        self.__findRecordsWindow.show_window()


    def __remove_records_by_date_and_time(self):
        self.__removeRecordsWindow = RemoveRecordsWindow()
        self.__removeRecordsWindow.show_window()


    



    def __open_file(self):
        fname = self.__getWorkFileName()
        
        if fname.encode('utf-8') != "":
            with open(fname, 'r') as file:
                    text = file.read().decode("utf-8")
                    self.__textEdit.setText(text)


    def __close_file(self):
        self.__textEdit.setText("")



    def __save_file(self):
        text    = self.__textEdit.toPlainText()
        fname   = self.__getWorkFileName()

        if fname.encode('utf-8') != "":
            with open(fname, 'w') as file:
                file.write(text)

    def __set_font(self):
        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            pass
            self.__textEdit.setFont(font)


    def __getWorkFileName(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '../reports/')
        return fname

    def close_window(self):
        QtCore.QCoreApplication.instance().quit()


    def show_window(self):
        self.show()

    
    



def initialization_application(app):

    autorizWind = AutorizationWindow()
    autorizWind.show_window()
    app.exec_()

    return autorizWind.is_autorization_successfully()
       


def main():
    app = QtGui.QApplication(sys.argv)

    if initialization_application(app) is False:
        sys.exit(-1)

    

    mainW = MainWindow(
        MAIN_WINDOW_TITLE, 
        DEFAULT_M_WINDOW_POS_Y,
        DEFAULT_M_WINDOW_POS_X
    )

    mainW.show_window()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    