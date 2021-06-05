#! /usr/bin/env python
#-*-coding: utf-8-*-


from widgetAttribute import *
from window import *
import sys

sys.path.append('../src/')
from record import Record
from dbDriver import DBDriver
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
