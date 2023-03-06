import os

os.system("")


def print_red(mess):
    print('\033[91m' + mess + '\033[0m')


def print_green(mess):
    print('\033[92m' + mess + '\033[0m')


def print_yellow(mess):
    print('\033[93m' + mess + '\033[0m')


def print_blue(mess):
    print('\033[94m' + mess + '\033[0m')


if __name__ == '__main__':
    print_red("red")
    print_green("green")
    print_yellow("yellow")
    print_blue("blue")
