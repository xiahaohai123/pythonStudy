tuple1 = (1, 2, 3, 4, 5)

print(tuple1)

# index 找下标 找不到会报错
print(tuple1.index(2))
# print(tuple1.index(20))  # ValueError: tuple.index(x): x not in tuple

# count 未找到返回0
tuple1 = (1, 1, 2, 3, 4, 5)
print(tuple1.count(1))  # 2
print(len(tuple1))  # 6

# 元组内不可变
# tuple1[0] = 100  # TypeError: 'tuple' object does not support item assignment

# 但是嵌套在内的可变集合内的数据还是可以变的s
tuple1 = (1, 1, 2, [3, 4], 5)
tuple1[3][0] = 100
print(tuple1)
