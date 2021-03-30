"""
打印空心正三角形
"""

count = int(input("请输入规模："))

i = 1
while i <= count:

    j = 0
    while j < count - i:
        print(" ", end="")
        j += 1

    j = 0
    while j < i * 2 - 1:
        if i != count:
            if j == 0 or j == i * 2 - 2:
                print("@", end="")
            else:
                print(" ", end="")
        else:
            print("@", end="")
        j += 1
    print()
    i += 1

"""
打印九九乘法表
"""

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}\t", end="")
    print()
