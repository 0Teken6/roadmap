import functools


def decorator_func(orig_func):
    @functools.wraps(orig_func)
    def wrapper(*args, **kwargs):
        print(f'Before executing {orig_func.__name__}')
        res = orig_func(*args, **kwargs)
        print(f"After executing {orig_func.__name__}")
        return res
    return wrapper


def second_dec(orig_func):
    @functools.wraps(orig_func)
    def wrapper(*args, **kwargs):
        print('+++++++++++++++')
        res = orig_func(*args, **kwargs)
        print('+++++++++++++++')
        return res
    return wrapper


@decorator_func
@second_dec
def some_func(line):
    print(f"Executing {some_func.__name__}: {line}")

some_func('HEllo')
