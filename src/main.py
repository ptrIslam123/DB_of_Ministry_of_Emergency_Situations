#! /usr/bin/env python
#-*-coding: utf-8-*-


from employees import Employees #
from shift import Shift #
from technic import Technic # 
from brigade import Brigade #
from geographLocation import GeographLocation
from vars import *


def main():
    b = Brigade()

    b.insert(
        "1",
        "10",
        "type1"
    )

    print(b.select_all_records())

    print("successful!")
    



if __name__ == "__main__":
    main()