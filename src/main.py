#! /usr/bin/env python
#-*-coding: utf-8-*-


from employees import Employees
from shift import Shift
from technic import Technic
from brigade import Brigade
from vars import *


def main():
    e = Employees()
    s = Shift()
    t = Technic()
    b = Brigade()
    print("successful!")
    



if __name__ == "__main__":
    main()