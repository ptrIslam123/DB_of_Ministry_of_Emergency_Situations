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


class FindRecordsWindow(BaseWindow):

    def __init__(self):
        super(FindRecordsWindow, self).__init__(
            FIND_WINDOW_TITLE,
            DEFAULT_FWINDOW_POS_X,
            DEFAULT_FWINDOW_POS_Y,
            DEFAULT_FWINDOW_WIDTH,
            DEFAULT_FWINDOW_HIGHT
        )
