#! /usr/bin/env python
#-*-coding: utf-8-*-


from widgetAttribute import *
from window import *
import sys

sys.path.append('../src/')
from autointoxication import Passwd, read_passwd_from_file
import errorHandler
import vars
import loger



AUTORIZATION_ERROR                  = 1
AUTORIZATION_SUCCESSFULLY           = 2
FAIL_ATTEMPT_AUTORIZATION           = 3 


class AutorizationWindow(BaseWindow):

    def __init__(self):
        super(AutorizationWindow, self).__init__(
            AUTORIZATION_WINDOW_TITLE,
            DEFAULT_AWINDOW_POS_X,
            DEFAULT_AWINDOW_POS_Y,
            DEFAULT_AWINDOW_WIDTH,
            DEFAULT_AWINDOW_HIGHT
        )

        self.__passwd       = read_passwd_from_file()
        self.__errHandler   = errorHandler.ErrorHandler() 
        self.__is_autorization_successfully = False
        self.__number_of_login_attempts = 0

        self.makeWindowDialog()



    def makeWindowDialog(self):
        self.__gridBox                  = QtGui.QGridLayout()

        user_login_lbl                  = QtGui.QLabel(AWINDOW_USER_LOGIN_LABEL)
        user_passwd_lbl                 = QtGui.QLabel(AWINDOW_USER_PASSWORD_LABEL)

        self.__user_login_ledit         = QtGui.QLineEdit()
        self.__user_passwd_ledit        = QtGui.QLineEdit()
        self.__status_ledit             = QtGui.QLineEdit()

        self.__autorization_btn         = QtGui.QPushButton(AWINDOW_AUTORIZATION_BUTTON)
        self.__cancel_btn               = QtGui.QPushButton(CANCLE_BTN_NAME)

        
        
        self.__gridBox.addWidget(user_login_lbl, 1, 1)
        self.__gridBox.addWidget(user_passwd_lbl, 2, 1)

        self.__gridBox.addWidget(self.__user_login_ledit, 1, 2)
        self.__gridBox.addWidget(self.__user_passwd_ledit, 2, 2)

        self.__gridBox.addWidget(self.__status_ledit, 3, 1)
        self.__gridBox.addWidget(self.__autorization_btn, 3, 2)
        self.__gridBox.addWidget(self.__cancel_btn, 3, 3)

        self.__autorization_btn.clicked.connect(self.__autorization_user)
        self.__cancel_btn.clicked.connect(self.close_window)

        self.setLayout(self.__gridBox)


    
    def __autorization_user(self):
        self.__number_of_login_attempts += 1

        if self.__number_of_login_attempts >= 5:
            self.__status_ledit.setText(self.__errHandler.handle(
                errorHandler.AUTORIZATION_ERORR, "Autorization window"
            ))
            exit(-1)

        user_login  = self.__user_login_ledit.text()
        user_passwd = self.__user_passwd_ledit.text()

        if self.__passwd.is_registrated_user() is False:
            self.__passwd.registration_new_user(user_login, user_passwd)

        self.__is_autorization_successfully = self.__passwd.autorization_user(user_login, user_passwd)
            
        if self.__is_autorization_successfully is True:
                self.close_window()
                return AUTORIZATION_SUCCESSFULLY
        else:
            self.__status_ledit.setText(self.__errHandler.handle(
                errorHandler.AUTORIZATION_ERORR, "Autorization window"
            ))
            return FAIL_ATTEMPT_AUTORIZATION
            



    def is_autorization_successfully(self):
        return self.__is_autorization_successfully