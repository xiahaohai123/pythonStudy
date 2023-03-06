"""
在类外添加对象属性
对象名.属性名=值
"""


class Student():
    def print_info(self):
        print(f"我叫{self.name}，现在{self.age}")


zhangshan = Student()
zhangshan.name = 'zhangshan'
zhangshan.age = 18
zhangshan.print_info()
print(f"我叫{zhangshan.name}，现在{zhangshan.age}")

"""
类内部设置属性
"""


class Teacher():
    name = str()
    age = 25

