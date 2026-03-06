import time
from turtle import st


def logging_decorator(function):
    def wrapper(*args):
        function(*args)
        arguments = [arg for arg in args]
        print(f"{function.__name__} {arguments}")

    return wrapper


@logging_decorator
def a_function(*args):
    mul = 1
    for arg in args:
        mul = mul * arg
    print(f"Answer {mul}")


def execution_time(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} = ", round(end_time - start_time, 4))

    return wrapper_function


@execution_time
def fast_function():
    time.sleep(3)


@execution_time
def slow_function():
    time.sleep(5)


# fast_function()
# slow_function()
a_function(1, 2, 3)
