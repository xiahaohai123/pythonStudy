import inspect
from typing import Callable


def curry(fn: Callable) -> Callable:
    len_in = len(inspect.signature(fn).parameters)
    cu_args = []

    def curried(*args):
        for arg in args:
            cu_args.append(arg)
        if len(cu_args) >= len_in:
            return fn(*cu_args)
        return curried

    return curried
