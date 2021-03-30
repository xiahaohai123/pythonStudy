# lambda 参数列表:表达式

def fun1():
    return 200


print(fun1())

fun2 = lambda: 200
print(fun2())

func3 = lambda a, b: a + b
print(func3(1, 2))

print((lambda a: a ** 2)(5))

# 默认参数
print((lambda a, b=100: a + b)(5))
print((lambda a, b=100: a + b)(5, 25))

print((lambda *args: args)([5, 25]))
print((lambda **kwargs: kwargs)(name='张山', age=18))

func4 = lambda a, b: a if a > b else b
print(func4(3, 9))

students = [
    {'name': 'zhangshan1', 'age': 18},
    {'name': 'zhangshan2', 'age': 15},
    {'name': 'zhangshan3', 'age': 13}
]

students.sort(key=lambda a: a['age'])
print(students)
