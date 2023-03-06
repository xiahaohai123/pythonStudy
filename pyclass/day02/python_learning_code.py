# 1.定义变量：存储数据TOM
my_name = 'TOM'
print('1.' + my_name)

'''
2.数据类型
  1)将不同的变量存储为不同的数据类型
  2）检测数据类型—— type()
'''
num1 = 1  # int 整型
num2 = 1.1  # float 浮点型
a = 'hello'  # string 字符串
b = True  # bool 布尔型——判断
c = [10, 20, 30]  # list 列表
d = (10, 20, 30)  # tuple 元组
e = {10, 20, 30}  # set 集合
f = {'name': 'TOM', 'age': '18'}  # dict 字典——键值对
print(type(num1))

'''
3.格式化输出
 %s——字符串 %d——有符号的十进制整数 %f——浮点数 %c——字符 
 %u——无符号整数
 %o——八进制整数 %x——十六进制整数 %e——科学计数法
tip.0
1.%03d,表示输出的整数显示位数，不足以0补全，超出当前位数则原样输出 %.2f，表示小数点后显示的小数位数。
2.格式化字符串除了%s，还可以写为 f'{表达式}'。
3.无符号且小于0的数据会执行以下代码
    if(x<0 && type == 'u'):
        type == 'd'
'''
age = 18
name = 'Jack'
weight = 75.5
stu_id = 1
print('3.my age is %d,my name is %s,my weight is %.2f,my id is %03d' % (age, name, weight, stu_id))
print('3.%s %s %s' % (name, weight, age))
print(f'3.my age is {age},my name is {name}')  # f'{表达式}'——高效(python3.6以后适用)

'''
4.转义字符
'\n' :换行
'\t' ：制表符，一个tab键（4个空格）的距离
5.结束符
py中，print()，默认自带 end="\n" 这个结束符，所以导致每两个print直接会还行展示，可按需更改
'''
print('4.\t hello \n python')
print('5.hello', end="\t")
print('5.制表符号', end="...!@##")

'''
6.输入&输出
input，等待用户输入完成后才继续向下执行，一般存储带变量，都当作字符串处理。

7.类型转换
int(x [,base])——将x转换为一个整数，float(x)——将x转换为一个浮点数，str(x)——将对象x转换为字符串
eval(str)——用来计算在字符串中的有效python表达式并返回一个对象，tuple(s)——将序列s转换为一个元组
list(s)——将序列转换为一个列表
ord(x)——将一个字符转换为它的ASCII整数值，hex(x)——将一个整数转换为一个十六进制字符串
oct(x)——将一个整数转换为一个八进制字符串，bin(x)——将一个整数转换为一个二进制字符串
'''
my_something = input('6.pls input something')
print(f'the text of input is {my_something}')
print(type(my_something))
print(type(int(my_something)))
str1 = '(100,20,30)'
print(type(eval(str1)))

'''
8.运算符
算数运算符(+,-,*,/,//——整除,%——取余，**——指数，()——小括号) (优先级：() > ** > * / // % > +-)
赋值( = 右赋左)（多个变量赋值： a,b,c = 10, 0.5, 'hello'）、复合赋值(算数+赋值)、比较（==,！=,<=,>=）
逻辑运算法(and,or,not)
tip.
1.and运算符，只要有一个值为0,则结果为0,，否则结果为最后一个非0数字
2.or运算符，只有所有值为0结果才为0,否则结果为第一个非0数字
'''
a_8 = 2 * 3 ** 2
print(a_8)  # 先指数再乘
print(not False)

# 9.条件语句 1)if…… 2)if……else…… 3)if……elif……else…… 4)if嵌套

age_9 = int(input('9.input u age: '))

if age_9 < 18:
    print(f'9.{age_9},too young,cannot go to bar')
elif (age_9 >= 18) and (age_9 <= 60):  # (age_9 >= 18) and (age_9 <= 60) 化简为 18<= age <=60
    print(f'9.{age_9}allow to go to bar')
else:
    print(f'9.{age_9},too old!')
print('9.not if')  # 无缩进，不算作if语句块中的代码

# 10.三目运算符 条件成立时执行的表达式 if 条件 else 条件不成立时执行的表达式
a_10 = 1
b_10 = 2
c_10 = a_10 if a_10 > b_10 else b_10
print('10.answer is ', c_10)

# 分割符号
print('\n\n----------------------------------------------------------------------\n\n')

'''
11.while循环语法
 break和continue是循环中满足一定条件退出循环的两种不同方式
 break——终止次循环， continue——退出当前一次循环继而执行下一次循环代码（记得修改计数器）
 whlie循环嵌套（从内写到外）
 else下方缩进的代码指的是当循环正常结束之后要执行的代码
'''
i_11 = 1
result_11 = 0
while i_11 <= 100:
    if i_11 % 2 == 0:
        result_11 += i_11
    i_11 += 1
print('11.even sum is ', result_11)

# 成法口诀表
a_11 = 1
while a_11 <= 9:
    b_11 = 1
    while b_11 <= a_11:
        print(f'{b_11}*{a_11}={b_11 * a_11}', end='\t')
        b_11 += 1
    print()
    a_11 += 1

'''
12.for循环
 for 临时变量 in 序列:
  重复执行的代码1……
 else下方缩进的代码指的是当循环正常结束之后要执行的代码
  else遇到break 不会执行代码，遇到continue 会
'''
# break和continue的比较
str_12 = '12.this is a test'
str_12_1 = '12.this is a test'
print('12.1test', end=' ')
for i_12 in str_12:
    if i_12 == 'i':
        break
    print(i_12, end='')
else:
    print('12.go to else')

print('\n12.2test', end=' ')
for i_12_1 in str_12_1:
    if i_12_1 == 'i':
        continue
    print(i_12_1, end='')
else:
    print('12.go to else')

'''
13.字符串详解
 -单引号、双引号、三引号 字符串中有’时 不要使用单引号或者使用\'(转义字符) 同理双引号
 -下标 从0开始顺序分配
 -切片 是指对操作的对象截取其中一部分的操作。 字符串、列表、元组都支持切片操作 (序列[开始位置下标：结束位置下标：步长])
tip.如果选取方向（从开始到结束的方向） 和 步长的方向冲突，则无法选取数据
-常用操作方法
-查找 find() 检测某个子串是否包含在字符串中，如果在返回下标，否则返回-1; index()与find()同理; count()出现的次数
 rfind(),rindex() 原理相同，从右侧开始查找。5个函数都是（子串，开始下标，结束下标）
-修改 replace(旧字符串，新字符串，替换次数)——原字符串的数据没更改（说明字符串是不可变类型）
 slit()-分割，返回一个列表
 join()语法 字符或子串.join(多字符串组成的序列)
 #转换
 capitalize():将字符串第一个字符转换成大写  title():将字符串每个单词的首字母转换成大写
 lower():字符串大写转小写  upper():字符串小写转大写
 #删除空白字符
 lstrip():删除左侧空白字符  retrip():删除右侧空白字符  strip():删除首尾空白字符
 #对齐
 ljust():左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串  rjust():右对齐 center():中间对齐
 字符串序列.ljust(长度，填充字符)
-判断(判读真假)
 startswitch():检查字符串是否以指定子串开头。设置开始结束下标就在指定范围内检查。startswitch(子串，开始下标，结束下标)
 endswitch():检查字符串是否以指定子串结束。同上
'''
str_13 = '    hello and world and abcDEFghi and Python    '
new_str_13 = str_13.replace('and', 'he')
list_13 = str_13.split('and', 2)
joinlist_13 = ['aa' , 'bb' , 'cc']
print('13.', str_13[-4:-1])  # 下标-1表示最后一个数据，依次向前类推
print('13.', str_13[2:5:1])  # 不写开始，默认从0开始;不写结束，默认取到最后;不写步长，默认为1;步长为负，表示倒取
print('13.', str_13[-4:-1:-1])  # 不能选取出数据，选取方向从左往右，-1步长从右往左
print('13.find实例 ', str_13.find('and', 10, 30))  # 结果为16
print('13.count test ', str_13.count('and'))  # 结果为3
print('13.replaced test', new_str_13)
print('13.split test', list_13)
new_joinstr_13 = '...'.join(joinlist_13)
print('13.new_joinstr ', new_joinstr_13)
print('13.new_capitalize_str ', str_13.capitalize())
print('13.new_title_str ', str_13.title())
print('13.new_strip_str ', str_13.strip())
test_str_13 = 'test'
print('13.new_ljust_str ', test_str_13.ljust(10, '?'))
print('13.new_endswitch_str ', str_13.endswith('Python'))

























