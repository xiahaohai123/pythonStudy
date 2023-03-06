"""
设置私有权限的方法
只需要在方法名前加上2个下划线
"""


class Person:
    def __init__(self):
        self.__name = 'zhangSan'

    def say(self):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


p = Person()
print(p.get_name())
