#! /usr/bin/env python
#-*-coding: utf-8-*-


from widgetNames import *
from window import *

class EditWindow(BaseWindow):

    def __init__(self):
        super(EditWindow, self).__init__(
            EDIT_WINDOW_TITLE,
            DEFAULT_EWINDOW_POS_X,
            DEFAULT_EWINDOW_POS_Y,
            DEFAULT_EWINDOW_WIDTH,
            DEFAULT_EWINDOW_HIGHT
        )
