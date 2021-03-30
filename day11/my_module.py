__all__ = ['sum1']
"""
all参数让该module被*号导入的时候只能使用all参数定义的方法
被特定导入的话all参数无效
from my_module import acc
"""


def sum1(a, b):
    print(a + b)


def acc(a, b):
    print(a * b)


if __name__ == '__main__':
    sum(1, 2)
