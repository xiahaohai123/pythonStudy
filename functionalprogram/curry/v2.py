import inspect
from typing import Callable


def curry(fn: Callable) -> Callable:
    len_in = len(inspect.signature(fn).parameters)

    def curried(*args):
        if len(args) >= len_in:
            return fn(*args)
        return curry_v2(fn, *args)

    return curried


def curry_v2(fn: Callable, *args) -> Callable:
    len_in = len(inspect.signature(fn).parameters)

    def curried_v2(*_args):
        cu_args = []
        for arg in args:
            cu_args.append(arg)
        for arg in _args:
            cu_args.append(arg)
        if len(cu_args) >= len_in:
            return fn(*cu_args)
        return curry_v2(fn, *cu_args)

    return curried_v2
