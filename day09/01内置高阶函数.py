# map()
"""
map(func,lst)将传入的函数变量func作用到lst变量中的每个元素，并将结果返回成新的map对象
"""
list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


print(type(map(func, list1)))
print(list(map(func, list1)))

print(list(map(lambda x: x ** 2, list1)))

# reduce()
"""
reduce(function(a,b),lst) 每次function计算的结果与序列的下一个元素进行计算
第一次取序列的前两个元素进行计算
"""
import functools

list1 = [1, 2, 3, 4, 5]


def func(a, b):
    return a + b


print(functools.reduce(func, list1))
print(functools.reduce(func, [1]))

# filter()

list1 = [i for i in range(11)]


def func(x):
    return x % 2 == 0


print(type(filter(func, list1)))
print(list(filter(func, list1)))
