s1 = {1, 2}

# s1.remove(1)
# s1.remove(1)  # s1.remove(1)  # 报错 KeyError: 1

s1.discard(1)
s1.discard(1)  # 不会报错
print(s1)

# pop 随机删除某个数据并返回 事实好像并不如此
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.pop())
print(s1)

# 因为是hash表 所以字符串比较明显
s1 = {"asd0", "zxc1", "afs2", "fgw4"}
print(s1.pop())
print(s1)
