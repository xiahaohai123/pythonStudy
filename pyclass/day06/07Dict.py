dict0 = {"name": "张三", "age": "18"}
print(dict0)
print(type(dict0))

# dict1 = dict()
# print(type(dict1))
# dict1 = {}
# print(type(dict1))

# 增加或修改
dict0['class'] = 'class_1'
dict0['name'] = '王五'
print(dict0)

# 删除
# del dict0['class']
# # del dict0['name 7']  # del dict0['name 7'] KeyError: 'name 7'
# print(dict0)
# dict0.clear()
# print(dict0)

# 查找
# key查找
print(dict0['name'])

# get() 对应java的get 和 getOrDefault
print(dict0.get('name'))
print(dict0.get('name', 18))
print(dict0.get('name1', 18))

# keys 返回所有的key
print(dict0.keys())
for i in dict0.keys():
    print(f"{i}-----{dict0[i]}")

# values
print(dict0.values())

# items
print(dict0.items())
for i, k in dict0.items():
    print(f"{i}------{k}")
