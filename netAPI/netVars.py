#! /usr/bin/env python
#-*-coding: utf-8-*-


SERVER_IP_ADDRESS                       = "192.168.0.14"
SERVER_PORT                             = 13000

SERVER_MAX_CONNECTIONS                  = 5

SERVER_DATA_BUF_SIZE                    = 1024

CLIENT_DATA_BUF_SIZE                    = SERVER_DATA_BUF_SIZE


PACKAGE_STD_SIZE                        = 10

NET_START_SERVER_EVENT                  = "STRAT SERVER"
NET_NEW_CONNECT_EVENT                   = "NEW_CONNECT" 
NET_CREATE_NEW_TASK_EVENT               = "CREATE NEW TASK"
NET_EXEC_NEW_TASK_EVENT                 = "EXECUTE NEW TASK"
NET_EXEC_METHOD_TYPE_TASK_EVENT         = "EXECUTE METHOD TYPE TASK"
NET_PROCESSING_REQUEST                  = "processing current request"
NET_CLOSE_CONNECTION_EVENT              = "CLOSE CONNECTION WITH CLIENT"
NET_CRITICAL_ERROR_EVENT                = "CRITICAL ERROR"
NET_UNDEFINE_ERROR                      = "undefine error"
NET_SCOKET_RECIVE_PACKAGE_ERROR         = "recive package error"
NET_REQUEST_UNDEFINE_METHOD_TYPE_EVENT  = "REQUEST UNDEFINE METHOD TYPE"
NET_SCOKET_BIND_ERROR_TYPE_EVENT        = "SOCKET BIND ERORR"
NET_CLIENT_CONNECT_ERROR_TYPE__EVENT    = "CONNECT ERROR"