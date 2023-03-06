# []

names = ['tom', 'jack', 'Wang']
objects = ['tom', 1, 'done', 6.0]

# 下标
print(names[0])
for o in objects:
    print(o, type(o))

# 查找
# print(names.index('lily'))  # 报错
print(names.index('tom'))
print(names.count('tom'))

# 获取长度
print("长度:", len(names))

# in
print('tom' in names)
print('lily' not in names)

# 增
# names.append('lily')  # ['tom', 'jack', 'Wang', 'lily']
# names.append(['lily', 'abc'])  # ['tom', 'jack', 'Wang', ['lily', 'abc']]
# print(names)

# names.extend('lily')  # ['tom', 'jack', 'Wang', 'l', 'i', 'l', 'y']
# names.extend(['lily', 'abc'])  # ['tom', 'jack', 'Wang', 'lily', 'abc']
# print(names)

# names.insert(1, 'lily')  # ['tom', 'lily', 'jack', 'Wang']
# print(names)

# 删除
# del names  # 报错
# del (names)  # 报错
# del names[0]  # ['lily', 'jack', 'Wang']
# print(names)

# pop 弹出指定下标的数据，默认为最后一个
# print(names.pop())  # Wang     ['tom', 'jack']
# print(names.pop(1))  # jack     ['tom', 'Wang']
# print(names)

names = ['tom', 'jack', 'Wang', 'tom', 'jack', 'Wang']
# remove 移除数据中第一个匹配项
# names.remove('tom')  # ['jack', 'Wang', 'tom', 'jack', 'Wang']
# print(names)

# names.clear()  # []
# print(names)

# 改
# names[0] = 'jack'  # ['jack', 'jack', 'Wang', 'tom', 'jack', 'Wang']a
# names[10] = 'change'  # 报错 IndexError: list assignment index out of range
# names.reverse()  # ['Wang', 'jack', 'tom', 'Wang', 'jack', 'tom']
# print(names)

nums = [1, 5, 6, 7, 5, 2, 3, 4, 8, 2, 66]
# nums.sort()  # [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 66]
# nums.sort(reverse=True)  # [66, 8, 7, 6, 5, 5, 4, 3, 2, 2, 1]
# print(nums)

# 复制 copy
print(nums.copy())  # nums = [1, 5, 6, 7, 5, 2, 3, 4, 8, 2, 66]

# objects.sort()
# print(objects)

# name_list = [
#     ['aa', 'bb'],
#     ['cc', 'dd'],
#     ['ee']
# ]
#
# for a in name_list:
#     for b in a:
#         print(b)


import random

names = ['甲', '乙', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']
class_room = [[], [], []]
for name in names:
    index = random.randint(0, 2)
    class_room[index].append(name)

print(class_room)
