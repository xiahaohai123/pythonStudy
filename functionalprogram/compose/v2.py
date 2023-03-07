from typing import Callable


def compose(*funcs: Callable) -> Callable:
    def composed_function(arg):
        result = arg
        for func in reversed(funcs):
            result = func(result)
        return result

    return composed_function
