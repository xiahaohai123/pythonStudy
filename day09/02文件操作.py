# 文件操作

#
"""
语法 open(name, mode)
    name：目标文件
    mode：打开文件的模式（读写追加）
"""
#
# f = open('testFile.txt', mode='w')
# f.write('abcdefghi\njklmn')
# # 将内容从buffer刷入到文件内
# f.flush()
#
# # 自动刷内容到文件内
# f.close()
#
# f = open('testFile.txt')
# # print(f.read(10))
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readline(2))  # ab
# # print(f.readlines())
# content = f.readline()
# while content:
#     print(content, end="")
#     content = f.readline()
#
# f.close()

# 读写
# f = open('cc.txt', mode='r+')  # 文件没有则报错，与r相同，+只是在原有的功能上增加操作，所以r+沿用r的特性

# 追加
# f = open('cc.txt', mode='a')  # 追加 会创建文件
# f.close()

# 追加可读
# f = open('cc.txt', mode='a+')
# f.close()

# seek 用来移动文件指针
"""
seek(self, offset: int, whence: int = 0)
语法：
    文件对象.seek(偏移量，起始位置)

    起始位置：
    0 文件开头
    1 当前位置
    2 文件结尾
"""
f = open('cc.txt', mode='a+')
f.seek(0)
print(f.readline(), end="")
f.close()
