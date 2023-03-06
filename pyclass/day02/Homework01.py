"""
1.%f格式化输出2位小数实现
"""
print("%.2f" % 1.0)
print("%.2f" % 2.000000)

"""
输入zhangshan 和 lisi，打印：zhangshan和lisi是同桌
"""
name0 = input("请输入张山的拼音:")
name1 = input("请输入李四的拼音:")
print(f"{name0}和{name1}是同桌\n")

"""
输入2个成绩，输出：最高分是{max}，最低分是{min}，平均分是{avg}
"""
score0 = float(input("请输入成绩1:"))
score1 = float(input("请输入成绩2:"))
# max = max(score0,score1)
print(f"最高分是{max(score0, score1)}")
print(f"最低分是{min(score0, score1)}")
print(f"平均分是{((score0 + score1) / 2)}")
