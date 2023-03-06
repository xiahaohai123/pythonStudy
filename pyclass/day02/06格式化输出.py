print("summer_sea无限进步", end='\n\t')

print("summer_sea无限进步", end="\n\n")

"""
    %s str
    %d 带符号的十进制整数
    %u 无符号的十进制整数
    %f 浮点型
"""
name = "summer_sea"
verb0 = "进步"
print("%s无限进步" % name, end='\n\t')
print("%s无限%s" % (name, verb0))

print("你的成绩是：%d，最高分是：%d" % (99, 150))
"""
无符号输出在遇到有符号的数据时会进入该条件
if (x < 0 && type == 'u') { 
    type = 'd'; 
}
"""
print("你的成绩是：%d，最高分是：%u" % (99, -150))
print("你的成绩是：%d，最高分是：%s" % (99, -150))

score = 99
max = 150
print(f"你的成绩是：{score}，最高分是：{max}")

"""
补齐
"""
number = 1
print("我的学号是：%010d" % number)
print("我的学号是：%02d" % number)

"""
小数点输出
"""
print("您的成绩是：%.2f" % score)
