"""
算术运算符   + - * / %
    //整除
    **指数
    ()提高优先级
赋值运算符   =
复合赋值运算符
比较运算符
逻辑运算符
"""

num0 = 100
num1 = num0
num0 = 90
print(num1)

str0 = "abc"
str1 = str0
str0 = "a"
print(str1)

# 多变量赋值
str1, str2, str3 = 1.5, 1, "c"
print(str1)
print(str2)
print(str3)

str1 = str2 = str3 = 1.5
print(str1)
print(str2)
print(str3)
