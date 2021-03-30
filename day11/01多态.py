"""
多态
"""


class A:
    def print_info(self):
        print('A')


class B(A):
    def print_info(self):
        print('B')


class C(A):
    def print_info(self):
        print('C')


class D:
    a = 10

    def func(self, a):
        a.print_info()


d = D()
d.func(C())
print(d.a)

d1 = D()
# d.a = 5  # 改变对象的值
D.a = 5  # 改变所有的值
print(d.a)
print(d1.a)
