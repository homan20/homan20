"""
    Напишите декоратор, который будет замедлять выполнение функции на 5 секунд.
    Если функция выполняется более 10 секунд (с учетом замедления), то
    дополнительно выводить сообщение f'{func.__name__} - very slow function'
"""

from functools import wraps
import time

def slow_down(seconds=1):
    def _slow_down(func):
        @wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper_slow_down
    return _slow_down

def timer(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - round(2))
        return res
    return wrapper


@slow_down(seconds=5)
@timer
def start():
    print('Start')


def bar():
    start()  
bar()
