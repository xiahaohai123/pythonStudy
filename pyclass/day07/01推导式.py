"""
列表推导式/列表生成式
"""
list2 = [i for i in range(10)]
print(list2)

list2 = [i for i in range(0, 10, 2)]
print(list2)

"""
带条件的列表推导式
"""
list2 = [i for i in range(10) if i % 2 == 1]
print(list2)

list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

list1 = ['name', 'age', 'sex']
list2 = ['zhangshan', 18, 'boy']
d = {list1[i]: list2[i] for i in range(len(list1))}
print(d)

d = {k: k * k for k in range(1, 6)}
d = {k: k ** 2 for k in range(1, 6)}
print(d)

d = {'zhangshan': 99, 'wangwu': 70, 'lisi': 58, 'aa': 30, 'bb': 100}
resD = {k: v for k, v in d.items() if v >= 60}
print(resD)

list3 = [{'name': 'zhangshan', 'age': 70},
         {'name': 'wangwu', 'age': 15},
         {'name': 'lisi', 'age': 17}]
resList = [i for i in list3 if dict(i)['age'] >= 18]
print(resList)

# 集合推导式
list1 = [1, 1, 2]
print({i ** 2 for i in list1})
