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

