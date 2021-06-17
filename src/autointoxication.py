#! /usr/bin/env python
#-*-coding: utf-8-*-

import hashlib
import pickle
from vars import PASSWD_FILE_PATH


class Passwd:

    def __init__(self):
        self.__user_login               = None
        self.__user_passwd_hash         = None
        self.__is_registrated_user      = False


    def registration_new_user(self, login, passwd):
        if self.__is_registrated_user is True:
            return False

        self.__user_login               = login
        self.__user_passwd_hash         = self.__get_hash(passwd)
        self.__is_registrated_user      = True


    def autorization_user(self, login, passwd):
        user_hash = self.__get_hash(passwd)

        if self.__user_login == login and self.__user_passwd_hash == user_hash:
            return True
        else:
            return False        


    def is_registrated_user(self):
        return self.__is_registrated_user


    


    def __get_hash(self, passwd):
        hash = hashlib.md5(passwd.encode())
        return hash.hexdigest()


    def __is_eq_hash(self, hash1, hash2):
        return hash1 == hash2


    def print_user(self):
        print(self.__user_login)
        print(self.__user_passwd_hash)

    
    


def write_passwd_in_file(passwd_obj):
    with open(PASSWD_FILE_PATH, 'wb') as file:
        pickle.dump(passwd_obj, file)


def read_passwd_from_file():
    with open(PASSWD_FILE_PATH, 'rb') as file:
        return pickle.load(file)



def main():
    user = Passwd()

    user.registration_new_user('islam', '12345')

    if user.autorization_user('islam', '12345') is True:
        print("successful!")
    else:
        print("fail!")


if __name__ == "__main__":
    main()