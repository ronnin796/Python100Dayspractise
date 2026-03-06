import time
from turtle import st


def execution_time(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print("Execution time = ", round(end_time - start_time, 4))

    return wrapper_function


@execution_time
def fast_function():
    time.sleep(3)


@execution_time
def slow_function():
    time.sleep(5)


fast_function()
slow_function()
