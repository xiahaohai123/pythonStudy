"""
__init__()
"""

# class Student():
#
#     # 不能重载
#     # def __init__(self):
#     #     self.name = 'zhangshan'
#     #     self.age = 18
#     #     print('init方法被调用')
#
#     def __init__(self, name, age):
#         self.name = 'name'
#         self.age = age
#         print('init方法被调用')
#
#     def say(self):
#         print(f"我叫{self.name}，现在{self.age}岁")
#
#
# zhangshan = Student('zhangshan', 18)
# # zhangshan.__init__('zhangshan', 18)  # 在3.8版本中可以外部调用 奇怪
# zhangshan.say()

"""
__str__
print(对象)
没有定义此方法，默认打印内存的地址值
如果定义了，则打印此方法内返回的产生的str
"""


class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('init方法被调用')

    def __str__(self):
        return f"name={self.name},age={self.age}"

    def __del__(self):
        print("被删除了")

    def say(self):
        print(f"我叫{self.name}，现在{self.age}岁")


zhangshan = Student('zhangshan', 18)
print(zhangshan)
del zhangshan

"""
__del__
程序结束默认调用的方法
del 对象也会触发
"""
