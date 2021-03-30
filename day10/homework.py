# 求出某个盘下有多少个文件，多少个文件夹

import os


def sub_file_num(path):
    print(path)
    os.chdir(path)
    file_list = os.listdir()

    # print(file_list)
    file_num = 0
    dir_num = 0
    for subPath in file_list:
        if subPath == '$RECYCLE.BIN':
            continue
        if os.path.isdir(subPath):
            dir_num += 1
            sub_tuple = sub_file_num(subPath)
            file_num += sub_tuple[0]
            dir_num += sub_tuple[1]
        else:
            file_num += 1
    # 回溯
    os.chdir('../')
    return file_num, dir_num


print(sub_file_num('./'))
