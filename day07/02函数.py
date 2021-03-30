"""
函数定义
def 函数名(参数):
    代码块

函数调用
函数名(参数) 

注意点：
代码自上而下解读
所以函数必须先定义后使用 
"""


def print_menus():
    print('1、查询')
    print('2、取款')
    print('3、存款')
    print('4、退卡')


print_menus()


def lei_jia(a, b):
    return a + b


print(lei_jia(1, 2))
