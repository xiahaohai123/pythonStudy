"""
类方法
@classmethod
cls
"""


class Dog:
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

    @staticmethod
    def print_info():
        print('这是一条狗')


d = Dog()
print(d.get_tooth())
Dog.print_info()
