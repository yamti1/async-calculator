import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor

default_executor = ThreadPoolExecutor()


def run_in_executor(
        executor=default_executor,
        condition=lambda *_, **__: True):
    """
    A decorator that runs the decorated function in an executor.
    :param executor: Optional. The executor to run the function in.
        Defaults to a ThreadPoolExecutor.
    :param condition: Optional. A function to determine if the function should run in the executor or not.
        Gets the wrapped function's arguments as arguments and should return True or False.
        Defaults to always run in executor.
    """
    def wrapper(func):
        async def wrapped(*args, **kwargs):
            if not condition(*args, **kwargs):
                return func(*args, **kwargs)
            return await asyncio.get_running_loop().run_in_executor(executor, partial(func, *args, **kwargs))
        return wrapped
    return wrapper
