"""
Java
    while(condition)

Python
    while condition :
        代码块
"""

# a = 1
#
# while a < 10:
#     print("while循环")
#     a += 1
#
# i = 0
# while i <= 100:
#     print(i)
#     i += 2

count = int(input("请输入规模："))
# i = 1
# while i <= count:
#     print(" " * (count - i), end="")
#     print("@ " * i)
#     i += 1
#
# i = count
# while i > 0:
#     print(" " * (count - i), end="")
#     print("@ " * i)
#     i -= 1

i = 1
while i <= count:
    # print(" " * (count - i), end="")

    # for j in range(0, count - i):
    #     print(" ", end="")

    j = 0
    while j < count - i:
        print(" ", end="")
        j += 1
    # print("@" * (i * 2 - 1))

    # for j in range(0, i * 2 - 1):
    #     print("@", end="")
    # print()

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
