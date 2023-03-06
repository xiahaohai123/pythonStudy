import os

# 文件重命名rename(目标文件名，新文件名)
# open('aaa.txt', 'w')
# os.rename('aaa.txt', 'bbb.txt')

# 删除文件remove(目标文件名)
# os.remove('bbb.txt')

# 创建文件夹mkdir('文件夹名称')
# os.mkdir('文件夹')

# 删除文件夹rmdir('文件夹名称')
# os.rmdir('文件夹')

# 获取当前目录getcwd() linux命令:pwd
print(os.getcwd())

# listdir()
print(os.listdir())

# 改变默认路径 chdir() change_directory
# os.chdir('D:/')
# print(os.listdir())

print(os.path.isfile('aaa.txt'))
os.chdir('../')
print(os.getcwd())
