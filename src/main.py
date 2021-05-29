#! /usr/bin/env python
#-*-coding: utf-8-*-


from employees import Employees #
from shift import Shift #
from technic import Technic
from brigade import Brigade
from geographLocation import GeographLocation
from vars import *


def main():
    t = Technic()

    t.insert(
        "1",
        "12",
        "type1",
        "kardsnov",
        "islam",
        "ibragimovich"
    )

    print(t.select_all_records())

    print("successful!")
    



if __name__ == "__main__":
    main()