# a = int(input("请输入a："))
# b = int(input("请输入b："))
#
# print(a + b)

str1 = "1"
print(type(str1))
num = int(str1)
print(type(num))

str1 = "1.5"
print(type(str1))
num = float(str1)
print(type(num))

num = 10000000000000000000000000000000000000000000
num1 = 2
num2 = 10000
print(type(num))
print(id(num))
print(num)

l = [1, 2, 3, 4, 5, 6, 6]
t = tuple(l)
s = set(l)
print(tuple(l))
print(type(t))
print(list(t))
print(s)

# eval(str) 自动识别类型
print("\n自动识别类型")
str1 = "10"
str2 = "[1,2,3]"
str3 = "(1,2,3)"
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))
