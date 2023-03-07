from typing import Callable


def compose(f, g: Callable) -> Callable:
    def composed_function(arg):
        return f(g(arg))

    return composed_function
