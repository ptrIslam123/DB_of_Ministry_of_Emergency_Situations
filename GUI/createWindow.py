#! /usr/bin/env python
#-*-coding: utf-8-*-

from widgetNames import *
from window import *

class CreateWindow(BaseWindow):

    def __init__(self):
        super(CreateWindow, self).__init__(
            CREATE_WINDOW_TITLE,
            DEFAULT_CWINDOW_POS_X,
            DEFAULT_CWINDOW_POS_Y,
            DEFAULT_CWINDOW_WIDTH,
            DEFAULT_M_WINDOW_HIGHT
        )

        self.__district_departue_list = [
            "district1", "district2", "district3"
        ]

        self.____visit_type_list = [
            "visit_t1", "visit_t2", "visit_t3"
        ]

        self.____additional_data_list = [
            "additional1", "additional2", "additional3"
        ]

        self.____sender_technics_list = [
            "sender1", "sender2"
        ]

        self.____rank_list = [
            "rank1", "rank2"
        ]

        self.makeWindowDialog()

    
    def makeWindowDialog(self):
        self.__gridBox  = QtGui.QGridLayout()

        self.__write_btn = QtGui.QPushButton(CWINDOW_WRITE_BTN_NAME)
        self.__cancel_btn = QtGui.QPushButton(CANCLE_BTN_NAME)



        district_departue_lbl   = QtGui.QLabel(CWINDOW_DISTRICT_DEPARTUE_LABEL)
        address_lbl             = QtGui.QLabel(CWINDOW_ADDRESS_LABEL)
        visit_type_lbl          = QtGui.QLabel(CWINDOW_VISIT_TYPE_LABEL)
        additional_data_lbl     = QtGui.QLabel(CWINDOW_ADDITIONAL_DATA_LABEL)
        sender_technics_lbl     = QtGui.QLabel(CWINDOW_SENDED_TECHNICS_LABEL)
        rank_lbl                = QtGui.QLabel(CWINDOW_RANK_LABEL)
        message_lbl             = QtGui.QLabel(CWINDOW_MESSAGE_LABEL)


        self.__district_departue_ledit   = QtGui.QComboBox()
        self.__district_departue_ledit.addItems(
            self.__district_departue_list
        )

        self.__address_ledit             = QtGui.QLineEdit()
        self.__visit_type_ledit          = QtGui.QComboBox()
        self.__visit_type_ledit.addItems(
            self.____visit_type_list
        )

        self.__additional_data_ledit     = QtGui.QComboBox()
        self.__additional_data_ledit.addItems(
            self.____additional_data_list
        )

        self.__sender_technics_ledit     = QtGui.QComboBox()
        self.__sender_technics_ledit.addItems(
            self.____sender_technics_list
        )
        self.__rank_ledit                = QtGui.QComboBox()
        self.__rank_ledit.addItems(
            self.____rank_list
        )
        self.__message_ledit             = QtGui.QTextEdit()



        self.__gridBox.addWidget(district_departue_lbl, 1, 1)
        self.__gridBox.addWidget(address_lbl, 2, 1)
        self.__gridBox.addWidget(visit_type_lbl, 3, 1)
        self.__gridBox.addWidget(additional_data_lbl, 4, 1)
        self.__gridBox.addWidget(sender_technics_lbl, 5, 1)
        self.__gridBox.addWidget(rank_lbl, 6, 1)
        self.__gridBox.addWidget(message_lbl, 7, 1)

        self.__gridBox.addWidget(self.__district_departue_ledit, 1, 2)
        self.__gridBox.addWidget(self.__address_ledit, 2, 2)
        self.__gridBox.addWidget(self.__visit_type_ledit, 3, 2)
        self.__gridBox.addWidget(self.__additional_data_ledit, 4,  2)
        self.__gridBox.addWidget(self.__sender_technics_ledit, 5, 2)
        self.__gridBox.addWidget(self.__rank_ledit, 6, 2)
        self.__gridBox.addWidget(self.__message_ledit, 8, 1)

        self.__gridBox.addWidget(self.__write_btn, 9, 3)
        self.__gridBox.addWidget(self.__cancel_btn, 9, 4)


        self.setLayout(self.__gridBox)

        self.__write_btn.clicked.connect(self.write_record_in_the_db)
        self.__cancel_btn.clicked.connect(self.close_window)



    def write_record_in_the_db(self):
        pass


