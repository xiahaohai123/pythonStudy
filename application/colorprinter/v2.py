import os
from functionalprogram.curry.v2 import curry

os.system("")


@curry
def color_print(color_code, mess: str):
    print('\033[' + color_code + mess + '\033[0m')


print_red = color_print("91m")
print_green = color_print("92m")
print_yellow = color_print("93m")
print_blue = color_print("94m")

if __name__ == '__main__':
    print_red("red")
    print_green("green")
    print_yellow("yellow")
    print_blue("blue")
