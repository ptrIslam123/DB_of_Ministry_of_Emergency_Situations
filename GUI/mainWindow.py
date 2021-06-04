#! /usr/bin/env python
#-*-coding: utf-8-*-

from PySide import QtGui, QtCore
from widgetNames import * 
import sys



class MainWindow(QtGui.QMainWindow):

    def __init__(self, titile, pos_x, pos_y, \
                width=DEFAULT_M_WINDOW_WIDTH, hight=DEFAULT_M_WINDOW_HIGHT):
        super(MainWindow, self).__init__()

        self.__title = titile
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__width = width
        self.__hight = hight

        
        
        self.__initUI()
        self.__createMenu()


    def __initUI(self):
        self.setGeometry(
            self.__pos_x, 
            self.__pos_y, 
            self.__width, 
            self.__hight
        )

        self.setWindowTitle(self.__title)



    def __createMenu(self):
        self.__action_open_file     = QtGui.QAction(MENU_FIELD_OPEN_FILE, self)
        self.__action_close_file    = QtGui.QAction(MENU_FIELD_CLOSE_FILE, self)
        self.__action_save_file     = QtGui.QAction(MENU_FIELD_SAVE_AS_FILE, self)
        
        self.__action_close_app     = QtGui.QAction(MENU_FIELD_EXIT_APP, self)
        
        self.__action_edit_file     = QtGui.QAction(MENU_FIELD_EDIT_FILE, self)
        self.__action_create_file   = QtGui.QAction(MENU_FIELD_CREATE_FILE, self)
        
        self.__action_set_font      = QtGui.QAction(MENU_FIELD_EDIT_FONT, self)

        self.__action_open_file.triggered.connect(self.__open_file)
        self.__action_close_file.triggered.connect(self.__close_file)
        self.__action_save_file.triggered.connect(self.__save_file)
        self.__action_close_app.triggered.connect(self.__close_window)
        self.__action_edit_file.triggered.connect(self.__edit_file)
        self.__action_create_file.triggered.connect(self.__create_file)
        self.__action_set_font.triggered.connect(self.__set_font)

        self.__menubar              = self.menuBar()

        self.__file                 = self.__menubar.addMenu(MENU_FIELD_ACTION_FILE) 
        self.__edit                 = self.__menubar.addMenu(MENU_FIELD_ACTION_EDIT)
        self.__view                 = self.__menubar.addMenu(MENU_FIELD_ACTION_VIEW)
        self.__create               = self.__menubar.addMenu(MENU_FIELD_ACTION_CREATE)


        self.__file.addAction(self.__action_create_file)
        self.__file.addAction(self.__action_save_file)
        self.__file.addAction(self.__action_close_file)

        self.__edit.addAction(self.__action_edit_file)

        self.__create.addAction(self.__action_create_file)

        self.__view.addAction(self.__action_set_font)


    
    def __open_file(self):
        print("open file!")

    def __close_file(self):
        print("close file!")

    def __save_file(self):
        print("save file!")

    def __edit_file(self):
        print("edit file!")

    def __create_file(self):
        print("creaet file!")

    def __edit_font(self):
        print("edit font!")

    def __set_font(self):
        font, ok = QtGui.QFontDialog.getFont()

        if ok:
            pass
            #self.__textEdit.setFont(font)


    def __close_window(self):
        QtCore.QCoreApplication.instance().quit()

    def show_window(self):
        self.show()

    
    


       


def main():
    app = QtGui.QApplication(sys.argv)
    
    mWindow = MainWindow(
        MAIN_WINDOW_TITLE, 
        DEFAULT_M_WINDOW_POS_Y,
        DEFAULT_M_WINDOW_POS_X
    )

    mWindow.show_window() 
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()