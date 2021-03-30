"""
继承 单继承
class 类名(继承的类):
    代码
"""


class A(object):
    def __init__(self):
        self.num = 1
        print("init A")

    def print_info(self):
        print(self.num)


class B(A):
    def __init__(self):
        A.__init__(self)
        print("init B")


a = A()
b = B()
# b.print_info()
# print(b.num)

"""
多继承
"""


class KeyBoard():
    info = 'keyBoard'

    def print_info(self):
        print("打字")


class Monitor():
    info = 'monitor'

    def print_info(self):
        print("我可以显示内容")


class Computer(Monitor, KeyBoard):
    pass


c = Computer()
# 当多继承时，两个父类拥有相同的方法或域时，先被继承的方法或域会被保留
c.print_info()
print(c.info)

"""
子类重写父类的方法和属性
"""


class Dog:
    def __init__(self):
        self.name = 'dog'

    def shout(self):
        print("shout")


class Zhtyq(Dog):
    def shout(self):
        # 取得超类
        super(Zhtyq, self).shout()
        super().shout()
        print("aowww")


z = Zhtyq()
z.shout()

d = Dog()
d.shout()
