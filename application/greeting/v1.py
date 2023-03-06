def greet(greeting, name: str) -> str:
    return f"{greeting} {name}"


if __name__ == '__main__':
    greeting_morning = "Good morning,"
    print(greet(greeting_morning, "Sam"))
    print(greet(greeting_morning, "Lily"))
