#! /usr/bin/env python
#-*-coding: utf-8-*-


from clientDB import *
import sys

sys.path.append('../src/')

from record import Record



def test_make_record():
    rec = Record()
    rec.set_date("22.22.25")
    rec.set_time("22:25")
    rec.set_rank("1")

    return rec


def perror(error_msg):
    print(error_msg)
    exit(-1)


def print_package(pkg):
    print("\n{")
    print("method_type: ", pkg.get_method_type())
    print(pkg.get_data())
    print("}\n")



def test_create_new_record(client, package):
    client.send_package(package)
    res_pkg, res = client.recive_package()

    if res != 0:
        perror("recive package error")

    return res_pkg



def test_get_all_records_from_db(client):
    client.send_package(
        make_get_all_records_from_db_package()
    )

    pkg, res = client.recive_package()
    
    if res != 0:
        perror("recive package error")
    
    else:
        return pkg



def test_find_record_by_date_and_time_request(client, date, time):
    client.send_package(
        Package(
            FIND_RECORDS_PACKAGE_METHOD_TYPE,
            "{date}\n{time}".format(date=date, time=time)
        )
    )

    res_pkg, res = client.recive_package()

    if res != 0:
        perror("recive package error")

    else:
        return res_pkg


def test_icmp(client, msg):
    client.send_package(
        make_icmp_packaget(msg)
    )

    pkg, res = client.recive_package()
    if res != 0:
        perror("recive package erorr from server")

    else:
        return pkg


