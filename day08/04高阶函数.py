print(abs(-19))


def add(a, b):
    return abs(a) + abs(b)


def add2(a, b, f):
    return f(a) + f(b)


print(add2(-1, -2, abs))
