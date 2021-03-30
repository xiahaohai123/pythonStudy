"""
运算符 作用 支持的类型
+     合并    字符串、列表、元组
*     复制    字符串、列表、元组
in      判断元素是否存在    字符串、列表、元组、字典
not in  判断元素是否不存在   字符串、列表、元组、字典
"""

"""
++++++++++++++++
"""
str1 = 'abc'
str2 = 'def'
num1 = 1

print(str1 + str2)
# print(str1 + num1)  # print(str1 + num1) TypeError: can only concatenate str (not "int") to str

list1 = [1, 2]
list2 = [10, 20]
print(list1 + list2)  # [1, 2, 10, 20]

t1 = (1, 2)
t2 = (10, 20)
print(t1 + t2)  # (1, 2, 10, 20)

s1 = {1, 2, 3}
s2 = {10, 20, 30}
# print(s1 + s2)  # print(s1 + s2) TypeError: unsupported operand type(s) for +: 'set' and 'set'


"""
***************
"""
str1 = '*'
print(str1 * 5)
print(['hello', 'world'] * 5)
print(('hello', 'world') * 5)

"""
in or not in
"""
print('a' in 'dfsfa')
print('a' not in 'dfsfa')

print([1, 2, 3] in [1, 2, 3, 4, 5, 6, 7])
print([1, 2, 3] in [[1, 2, 3], 1, 2, 3, 4, 5, 6, 7])
print([1, 2, 3] not in [[1, 2, 3], 1, 2, 3, 4, 5, 6, 7])

print((1, 2, 3) in (1, 2, 3, 4, 5, 6, 7))
print((1, 2, 3) in ((1, 2, 3), 1, 2, 3, 4, 5, 6, 7))
print((1, 2, 3) not in ((1, 2, 3), 1, 2, 3, 4, 5, 6, 7))

dict0 = {'name': '张三', 'age': 18}
# 针对key进行判断
print('张三' in dict0)
print('name' in dict0)

"""
公共方法
len() 计算序列里元素的个数
del/del() 删除
max() 返回最大值
min() 返回最小值
range(start,end,step) 供 for循环使用
enumerate() 将一个可遍历的数据对象（列表、元组、字符串）组合为一个索引序列
    同时列出数据和数据下标，一般用于for循环
"""

"""
len()
"""
print(len('abc'))
print(len([1, 2, 3, 4]))
print(len((1, 2, 3, 4)))
print(len({1, 2, 3, 4}))
print(len({'name': '张三', 'age': 18}))

"""
del()
"""

"""
range()
"""
a = range(0, 10, 1)
print(a)

for i in a:
    print(i)

"""
enumerate(可遍历对象，start=0)
"""
list1 = [1, 2, "abcdefg"]
a = enumerate(list1)
for i in a:
    print(i)

"""
类型转换
"""
list1 = [1, 2, "abcdefg"]
set1 = {1, 2, 3, 4}
print(tuple(list1))
print(tuple(set1))
# 字典只转key
print(tuple(dict0))

