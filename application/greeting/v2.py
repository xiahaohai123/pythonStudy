from application.greeting.v1 import greet


def greet_morning(name: str) -> str:
    return greet("Good morning,", name)


def greet_afternoon(name: str) -> str:
    return greet("Good afternoon,", name)


if __name__ == '__main__':
    print(greet_morning("Sam"))
    print(greet_afternoon("Lily"))
