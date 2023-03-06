"""
if 条件 :
    代码块1
    代码块2
"""

if True:
    print("aaa")
    print("bbb")
elif True:
    print("bac")
else:
    print("avd")

age = 23

if 18 < age < 50:
    print("可以上网")
elif age < 18:
    print("未成年人不许上网")
elif age > 50:
    print("老人年不许上网")

money = 1
site = 1

if money >= 2:
    money -= 2
    print("上车")
    if site >= 1:
        print("坐下")
        site -= 1
else:
    print("钱不够")
