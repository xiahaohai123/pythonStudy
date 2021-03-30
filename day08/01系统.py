"""
学员管理系统

1、添加学员
2、删除学员
3、修改学员信息
4、查询学员信息
5、显示出所有学员信息
6、退出系统

"""
student_number_k_name = '学号'
student_name_k_name = '姓名'
student_tel_k_name = '联系电话'
students = []


def print_menu():
    print("""
---------------------------
|   1、添加学员
|   2、删除学员
|   3、修改学员信息
|   4、查询学员信息
|   5、显示出所有学员信息
|   6、退出系统
---------------------------
""")


def show_all_students():
    print(students)


def add_student():
    number = input("请输入学号：")
    for i in students:
        if i['学号'] == number:
            print("该学号已经存在")
            return
    name = input("请输入姓名：")
    tel = input("请输入手机号：")

    d = dict()
    d[student_number_k_name] = number
    d[student_name_k_name] = name
    d[student_tel_k_name] = tel
    students.append(d)
    print(f"学员添加完成:{d}")


def look_up(number):
    has_found = False
    index = int()
    item = dict()
    for index, item in enumerate(students):
        if item['学号'] == number:
            has_found = True
            break
    if has_found:
        return index, item
    else:
        return has_found


def look_up_student():
    while True:
        number = input("请输入查询的学号(back返回)：")
        if number == 'back':
            break
        res = look_up(number)
        if res:
            print(res[1])
        else:
            print("未找到该学员，请重新输入")


def del_student():
    # 匹配到的信息可以全部删除或者逐条删除
    condition = input("请输入查找的字符串：")
    found_list = []
    numb = 1
    for index, item in enumerate(students):
        for value in dict(item).values():
            if str(value).find(condition) != -1:
                found_list.append(item)
                numb += 1
                break

    if len(found_list) == 0:
        print("未找到相应条目")
    else:
        print("已找到匹配条目")
        while True:
            if len(found_list) == 0:
                break
            for i, student in enumerate(found_list):
                print(i + 1, student)
            del_index = input("请输入需要删除的条目号(all全部删除、no取消)：")
            if del_index == 'no':
                print("取消删除")
                break
            elif del_index == 'all':
                for item in found_list:
                    students.remove(item)
                print("删除完毕")
                break
            else:
                try:
                    index = int(del_index) - 1
                except Exception:
                    print("输入的是非法值")
                else:
                    if index >= len(found_list):
                        print("输入编号过大")
                        continue
                    item = found_list[index]
                    students.remove(item)
                    del found_list[index]
                    print("删除完毕,跳转至主页面")

    # number = input("请输入需要删除的学员的学号：")
    # res = look_up(number)
    # if not res:
    #     print("未找到该学员")
    # else:
    #     print("已找到学员")
    #     print(res[1])
    #     while True:
    #         check = input("确定要删除吗(y/n)：")
    #         if check == 'yes' or check == 'y' or check == 'ye':
    #             del students[res[0]]
    #             print("已删除")
    #             break
    #         elif check == 'n' or check == 'no':
    #             print("不删除")
    #             break
    #         else:
    #             print("输入不正确，请重新输入")


def modify_student_info():
    while True:
        number = input("请输入需要修改的学员的学号(back返回)：")
        if number == 'back':
            break
        res = look_up(number)
        if not res:
            print("未找到该学员")
        else:
            print("已找到学员")
            print(res[1])

            while True:
                print("""
-------------
修改方式
-------------
1、修改所有
2、修改单个信息
3、显示当前修改学员信息
4、取消修改
-------------""")
                op_code = input("请输入编号以确定修改方式：")
                if op_code == '1':
                    number = input("请输入新的学号：")
                    find_res = look_up(number)
                    if find_res:
                        print("已存在相同的学号")
                    else:
                        name = input("请输入新的姓名：")
                        tel = input("请输入新的联系电话：")
                        res[1][student_number_k_name] = number
                        res[1][student_name_k_name] = name
                        res[1][student_tel_k_name] = tel
                        print("修改完成")
                        print(f"新的学员信息：{res[1]}")
                elif op_code == '2':
                    print("""
------------
修改对象
------------
1、学号
2、姓名
3、联系电话
4、显示当前修改学员信息
5、返回
------------""")
                    while True:
                        op_code = input("请输入编号以确定修改对象：")
                        if op_code == '1':
                            number = input('请输入新的学号：')
                            find_res = look_up(number)
                            if find_res:
                                print("已存在相同的学号")
                            else:
                                res[1][student_number_k_name] = number
                                print('修改完成')
                        elif op_code == '2':
                            name = input('请输入新的姓名：')
                            res[1][student_name_k_name] = name
                            print('修改完成')
                        elif op_code == '3':
                            tel = input('请输入新的联系电话：')
                            res[1][student_tel_k_name] = tel
                            print('修改完成')
                        elif op_code == '4':
                            print(res[1])
                        elif op_code == '5':
                            break
                        else:
                            print('命令输入错误，请重新输入')
                elif op_code == '3':
                    print(res[1])
                elif op_code == '4':
                    print("取消修改")
                    break
                else:
                    print("命令输入错误，请重新输入")


def operate(op_code):
    if op_code == '1':
        add_student()
    elif op_code == '2':
        del_student()
    elif op_code == '3':
        modify_student_info()
    elif op_code == '4':
        look_up_student()
    elif op_code == '5':
        show_all_students()
    else:
        print("输入值为要求外，请重新输入")


while True:
    print_menu()
    num = input("请输入对应编号以进行相应操作：")
    if num == '6':
        print('-' * 10)
        print("Good Bye!")
        break
    operate(num)
