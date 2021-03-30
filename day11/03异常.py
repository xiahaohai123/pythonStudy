"""
了解异常
"""

try:
    f = open('aaaaaaaaaaaaaaaaa.txt', 'r')
    # print(1 / 0)
except Exception as result:
    print('error')
    print(__name__)
    print(result)
else:
    print('我是else')
finally:
    f.close()
