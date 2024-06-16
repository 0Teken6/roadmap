from functools import wraps


def my_logger(func):
    import logging
    logging.basicConfig(filename=f'{func.__name__}.log', level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        print("Was added to log")
        return func(*args, **kwargs)
    return wrapper


def my_timer(func):
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t_delta = time.time() - t1
        print(f"Ran in {t_delta}")
        return res
    return wrapper

import time


@my_logger
@my_timer
def func(line):
    time.sleep(2)
    print(f'Func: {line}')


func('My bad')
