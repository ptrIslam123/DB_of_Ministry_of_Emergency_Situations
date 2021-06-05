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


class RemoveRecordsWindow(BaseWindow):

    def __init__(self):
        super(RemoveRecordsWindow, self).__init__(
            REMOVE_WINDOW_TITLE,
            DEFAULT_RWINDOW_POS_X,
            DEFAULT_RWINDOW_POS_Y,
            DEFAULT_RWINDOW_WIDTH,
            DEFAULT_RWINDOW_HIGHT
        )
