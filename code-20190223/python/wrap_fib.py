from functools import wraps


def memo(func):
    cache = dict()
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(n):
    return 1 if n < 2 else fib(n - 2) + fib(n - 1)


def my_memo(func):
    cache = dict()


if __name__ == "__main__":
    print(fib(100))
