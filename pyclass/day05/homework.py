import random

# 随机分配
names = ['甲', '乙', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']
class_room = [[], [], []]
for name in names:
    index = random.randint(0, 2)
    class_room[index].append(name)

print(class_room)

# 2
num = [5, 2, 55, 21, 43]
num[2] = 10
num.extend([2, 1, 5])
num.sort(reverse=True)
print(num)
