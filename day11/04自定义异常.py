class MyError(Exception):
    def __init__(self, length, min_length=3):
        self.length = length
        self.min_length = min_length

    def __del__(self):
        return f'您输入的密码长度为{self.length}，不能少于{self.min_length}'


i = input('请输入密码：')

try:
    if len(i) < 3:
        raise MyError(len(i))
except Exception as ex:
    print(ex)
