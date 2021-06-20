
#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket
from package import *


host = "192.168.0.12"
port = 12000


server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
)

server.bind((
        host, port
))

server.listen(5)



def send_package(client, package):
        packages = split_to_list_packages(package, 5)

        for pkg in packages:
                client.send(serialization(pkg))
                res_pkg = deserialization(client.recv(1024))

                if res_pkg.get_method_type() != SUCCESSFUL_PACKAGE_RESULT:
                        print("Eror: response.type: ", res_pkg.get_method_type())
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
                client, addr = server.accept()

        except KeyboardInterrupt:
                server.close()
                break

        else:
                try:
                        while True:
                                
                                pkg, res = recive_package(client)

                                if res != 0:
                                        client.close()
                                        print("recive__error: connection destroy__\n")
                                        break

                                print("[Client] type: ", pkg.get_method_type(), 'data: ', pkg.get_data())

                                res = send_package(client, pkg)

                                if res != 0:
                                        client.close()
                                        print("send__error: connection destroy__\n")
                                        break
                                

                except KeyboardInterrupt:
                        client.close()
                        break



'''
while True:
        try:
                client, addr = server.accept()

        except KeyboardInterrupt:
                server.close()
                break

        else:
                try:
                        while True:
                                
                                pkg = deserialization(client.recv(1024))
                                print("type: ", pkg.get_method_type(), 'data: ', pkg.get_data())
                                
                                client.send(serialization(Package(
                                        ICMP_PACKAGE_TYPE, "Ok"
                                )))
                                
                except KeyboardInterrupt:
                        client.close()
                        break
'''