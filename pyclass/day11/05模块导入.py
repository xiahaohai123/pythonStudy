"""
import 模块名
from 模块名 import 功能名
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
"""
#
# # import math
# from math import sqrt
#
# # print(math.sqrt(8))
# print(sqrt(9))

# import math as m
#
# print(m.sqrt(9))

# from math import *
#
# print(sqrt(9))

# import my_module
# my_module.sum(2, 2)

# from day11.my_module import *
#
# sum1(2, 1)
# # acc(1, 2)

import pyclass.day11.mypackage.my_module as md

md.print_info()

from pyclass.day11.mypackage import *

my_module.print_info()
