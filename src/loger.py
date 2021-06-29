#!/usr/bin/env python
#-*-coding: utf-8-*-

import os

import vars 
from datetime import datetime




def net_write_log(type_log, descr):
    write_log(vars.NET_SYSTEM_LOG_FILE_PATH, type_log, descr)


def sys_write_log(type_log, descr):
    write_log(vars.SQL_SYSTEM_LOG_FILE_PATH, type_log, descr)




def write_log(fname, type_log, descr):
    if os.path.exists(fname) == False:
        with open(fname, "w") as file:
            pass

    with open(fname, "a") as file:
        time = get_time()
        log = "{time}\t[{type_log}:\t{descr}]\n".format(
            time=time,
            type_log=type_log,
            descr=descr
        )

        file.writelines(
            log
        )


def get_time():
    return str(datetime.now())