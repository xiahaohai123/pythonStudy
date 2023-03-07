from application.colorprinter.v2 import *
from functionalprogram.compose.v1 import compose
from functionalprogram.curry.v2 import curry


def compose_tag_message(tag, message: str) -> str:
    return f"{tag} {message}"


create_output = curry(compose_tag_message)
greet = curry(compose_tag_message)

debug = compose(print_blue, create_output("[DEBUG]"))
info = compose(print_green, create_output("[INFO]"))
warn = compose(print_yellow, create_output("[WARN]"))
error = compose(print_red, create_output("[ERROR]"))


@curry
def trace(tag, message: str) -> str:
    output = create_output(tag, message)
    print(output)
    return message


if __name__ == '__main__':
    debug("this is a debug message")
    info("this is a info message")
    warn("this is a warn message")
    error("this is a error message")
