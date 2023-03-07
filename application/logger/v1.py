from application.colorprinter.v2 import *


def info(_message: str):
    output = f"[INFO] {_message}"
    print_green(output)


def debug(_message: str):
    output = f"[DEBUG] {_message}"
    print_blue(output)


def warn(_message: str):
    output = f"[WARN] {_message}"
    print_yellow(output)


def error(_message: str):
    output = f"[ERROR] {_message}"
    print_red(output)


if __name__ == '__main__':
    debug("this is a debug message")
    info("this is a info message")
    warn("this is a warn message")
    error("this is a error message")
