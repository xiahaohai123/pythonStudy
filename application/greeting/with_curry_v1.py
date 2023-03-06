from application.greeting.v1 import greet
from functionalprogram.curry.v1 import curry

curried_greet = curry(greet)
greeting_user_define = "Have a nice day,"
greet_user = curried_greet(greeting_user_define)


def common_use():
    print(greet_user("Sam"))


def err_use():
    print(greet_user("Sam"))
    print(greet_user("Linda"))


if __name__ == '__main__':
    err_use()
