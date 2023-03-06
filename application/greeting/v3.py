from typing import Callable
from application.greeting.v1 import greet


def curry_greet(greeting: str) -> Callable:
    def curried_greet(name: str) -> str:
        return greet(greeting, name)

    return curried_greet


greet_morning = curry_greet("Good morning,")
greet_afternoon = curry_greet("Good afternoon,")

# 假设这是用户保存在咱们系统中的输出，不管他来自哪，数据库，redis，甚至是一级缓存都可以
greeting_user_define = "Have a nice day,"
greet_user = curry_greet(greeting_user_define)

if __name__ == '__main__':
    print(greet_user("Sam"))
