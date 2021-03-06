#! /usr/bin/env python
#-*-coding: utf-8-*-

SQL_DB_DIR_PATH                 = "../sqlDB"
SQL_TABLES_DIR_PATH             = "../sqlTables"
SQL_SYSTEM_LOG_FILE_PATH        = "../sys/syslog.txt"
PASSWD_FILE_PATH                = "../sys/passwd.txt"
NET_SYSTEM_LOG_FILE_PATH        = "../sys/netsyslog.txt"
MAIN_SQL_DB_FILE                = "../sqlDB/main.db"
PATH_REPORTS_DIR                = "../reports"



# log types:
ERROR_LOG_TYPE                  = "CRITICAL ERROR"
WARNING_LOG_TYPE                = "WARNING"
EVENT_LOG_TYPE                  = "EVENT" 


# descriptions_type:
INSERT_DATA_INTO_THE_TABLE      = "Made the insert of data into the table => "
UPDATE_DATA_INTO_THE_TABLE      = "the data in the table was updated => "
REMOVE_DATA_INTO_THE_TABLE      = "deleted data from the table => "
SEARCH_DATA_INTO_THE_TABLE      = "the table was searched => "
RESPONSE_ERROR_FROM_SERVER      = ""
FAIL_SEND_PACKAGE_ON_SERVER     = ""