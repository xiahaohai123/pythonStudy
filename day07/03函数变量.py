# # b = 1000
# #
# #
# # def testA():
# #     print(id(b))
# #     print(b)
# #
# #
# # def testB():
# #     global b
# #     b = 2000
# #     print(id(b))
# #     print(b)
# #
# #
# # def testC():
# #     global c
# #     c = 3000
# #     print(id(c))
# #     print(c)
# #
# #
# # print(id(b))
# # testB()
# # testA()
# #
# # # print(id(c))  # 报错
# # # print(c)
# #
# # testC()
# # print(id(c))
# # print(c)
#
#
# # def test1():
# #     return 1
#
# # 默认元组
# def test1():
#     return {1, 2}
#
#
# # def test2(num):
# #     print(num)
# # test2(test1())
#
# # 传递方法
# def test2(method):
#     print(method())
#
#
# # 参数是方法名
# test2(test1)
#
#
# # # 位置参数 根据函数定义的位置来定义参数
# # def user_info(name, age, gender):
# #     print(f"{name}---{age}----{gender}")
# #
# #
# # user_info('zhangsan', 18, 'boy')
# #
# # # 关键字参数
# # user_info('埃尔德里奇', gender='girl', age='16')
#
# # 参数缺省
# def user_info(name, age, gender='男'):
#     print(f"{name}---{age}----{gender}")
#
#
# # 不定长元组参数
# def user_info(*args):
#     print(args)
#
#
# user_info('tom', 'lily')
#
#
# # 不定长字典
# def user_info(**kwargs):
#     print(kwargs)
#
#
# user_info(name='tom', age=18, sex='boy')
#
#
# def test1():
#     return 1, 2
#
#
# a, b = test1()
# print(a)
# print(b)

# 拆包
d = {'name': 'tom', 'age': 18, 'sex': True}
a, b, c = d
print(a)
print(b)
print(c)

a = 10
b = 20
# a = a + b
# b = a - b
# a = a - b

a, b = b, a
print(a)
print(b)

a = 10
b = a
print(id(a))
print(id(b))
