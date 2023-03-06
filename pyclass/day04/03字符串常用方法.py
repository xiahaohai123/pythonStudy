# 查找
# find() 找不到返回-1
a = 'abcdefghijklmnopqrstuvwxyz'
print(a.find('bcd'))
print(a.find('bcd', 4))
print(a.find('bcd', 5, 10))
print(a.find('jk', 5, 11))
print(a.find('jk', 5, 10))
# rfind() 从右往左查
print(a.rfind('jk', 5, 11))

# index() 找不到报错
# print(a.index('jk', 5, 10))
print(a.rindex('jk'))

# count() 返回某个字符串在字符串中出现的次数
a = "aaaaacccccvacvaacccav"
print(a.count("v"))

# 修改
# replace()
a = 'acc'
print(a.replace('c', 'a'))
print(a.replace('c', 'a', 1))
print(a)

# split()
a = "hello ! python !"
print(a.split(" "))
print(a.split(" ", 1))
print(a.split(" ", 5))

# join()
b = a.split(" ")
print(".....".join(b))

# 大小写
print(a.capitalize())
print(a.title())
print(a.upper())
print(a.lower())

# 去除空格
b = '      c b s       '
print(b.lstrip())
print(b.rstrip())
print(b.strip())

# 判断
# startswith
a = "hello python"
print(a.startswith("h"))
print(a.startswith("e", 1))
print(a.startswith("e", 2))
print(a.startswith("el", 1, 2))
print(a.startswith("el", 1, 3))
print(a.endswith("n"))

# isalpha() 字符串中至少有一个字符并且全部是字母则返回True 否则False
# isdigit()
# isalnum() 字母或数字
print("hello".isalpha())
print("hello ".isalpha())
print("123".isdigit())
print("12 3".isdigit())
print("123abc".isalnum())
print("123abc.".isalnum())

print("1 3 5 4 8 6 8 ".isspace())
print("              ".isspace())
