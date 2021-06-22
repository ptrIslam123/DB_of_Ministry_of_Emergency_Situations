#! /usr/bin/env python
#-*-coding: utf-8-*-


from clientDB import *



def perror(error_msg):
    print(error_msg)
    exit(-1)


def print_package(pkg):
    print("\n{")
    print("method_type: ", pkg.get_method_type())
    print(pkg.get_data())
    print("}\n")





def test_get_all_records_from_db(client):
    client.send_package(
        make_get_all_records_from_db_package()
    )

    pkg, res = client.recive_package()
    
    if res != 0:
        perror("recive package error")
    
    else:
        return pkg



def test_icmp(client, msg):
    client.send_package(
        make_icmp_packaget(msg)
    )

    pkg, res = client.recive_package()
    if res != 0:
        perror("recive package erorr from server")

    else:
        return pkg


'''
import socket
from package import *

host = "192.168.0.12"
port = 12000


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((
    host, port
))


def send_package(client, package):
    packages = split_to_list_packages(package, 5)

    for pkg in packages:
        client.send(serialization(pkg))
        res_pkg = deserialization(client.recv(1024))

        if res_pkg.get_method_type() != SUCCESSFUL_PACKAGE_RESULT:
            print("Erro: response.type: ", res_pkg.get_method_type())
            client.close()
            return -1

        print("\t***send-successful***")
            
    return 0



def recive_package(client):
    packages = []

    while True:

        pkg = deserialization(client.recv(1024))


        if pkg.get_method_type() == LAST_PACKAGE_TYPE:
            client.send(serialization(
                Package(SUCCESSFUL_PACKAGE_RESULT, "Ok")
            ))
            break
        
        packages.append(pkg)
        print("***recive-successful***")

        client.send(serialization(
            Package(SUCCESSFUL_PACKAGE_RESULT, "Ok")
        ))
    
    return join_to_one_package(packages), 0

        

while True:
    try:
        pkg = Package(ICMP_PACKAGE_TYPE, raw_input(">"))

        res = send_package(client, pkg)
        
        if res != 0:
            client.close()
            print("send__error: connection destroy__\n")
            break

        pkg, res = recive_package(client)

        if res != 0:
            client.close()
            print("recive__error: connection destroy__\n")
            break

        print("[Server] type: ", pkg.get_method_type(), 'data: ', pkg.get_data())

    except KeyboardInterrupt:
        client.close()
        break



client.close()
'''