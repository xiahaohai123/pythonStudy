"""
    写一个学员管理系统

    1、添加学员
    2、删除学员
    3、修改学员信息
    4、查询学员信息
    5、显示所有学员信息
    6、退出系统

"""


def print_info():
    print('-' * 20)
    print('1、添加学员')
    print('2、删除学员')
    print('3、修改学员信息')
    print('4、查询学员信息')
    print('5、显示所有学员信息')
    print('6、退出系统')
    print('-' * 20)


info = []


def add_info():
    """ 添加学员 """

    global info
    number = input('请输入学号：')
    name = input('请输入姓名：')
    tel = input('请输入手机号：')

    for i in info:
        if name == i['name']:
            print('该用户已经存在')
            return
    d = {}
    d['name'] = name
    d['number'] = number
    d['tel'] = tel

    info.append(d)


def show_all():
    print(info)


def del_info():
    """ 删除学员信息 """
    global info
    number = input('请输入您要删除的学生学号')

    # 1、如果学号存在重复的，如何全部删完

    for i, k in enumerate(info):
        if number == k['number']:
            del info[i]
            return


def modify_info():
    """ 修改学员信息 """

    number = input('请输入要修改学生的学号')

    # 2、实现 当输入学员不存在的时候，提示错误信息后，然后让用继续输入
    for i in info:
        if number == i['number']:
            i['number'] = input('请输入学号')
            i['name'] = input('请输入姓名')
            i['tel'] = input('请输入手机号')
            return


while True:
    # 显示功能界面
    print_info()
    # 用户选择对应功能
    num = input('请选择您要的操作:')
    if num == '1':
        # print('添加学员')
        add_info()
    elif num == '2':
        print('删除学员')
    elif num == '3':
        print('修改学员信息')
    elif num == '4':
        print('查询学员信息')
    elif num == '5':
        # print('显示所有学员信息')
        show_all()
    elif num == '6':
        # print('退出系统')
        break
    else:
        print('您输入错误，请重新输入...')
