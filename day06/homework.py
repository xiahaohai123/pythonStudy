"""
1
"""
list1 = [1, 23, 62, 12, 1, 3, 223, 12, 315]
print(set(list1))

"""
2
"""
dict0 = {'name': 'zhangshan', 'age': 20, 'sex': 'boy'}
for k, v in dict0.items():
    print(f"{k}--------{v}")

"""
3
"""
list2 = ['name', 'age', 'sex']
list3 = ['zhangshan', 20, 'boy']

dict2 = {}
for index, key in enumerate(list2):
    dict2[key] = list3[index]

print(dict2)
