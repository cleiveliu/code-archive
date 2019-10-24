
# source https://eastlakeside.gitbooks.io/interpy-zh/content/func_caching/python_2.html
# 函数的缓存
from functools import wraps


def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(100))

"""
This code may cause max recursion deep **
```python
def fib(n):
    return [0,1][n] if n < 2 else fib(n-2)+fib(n-1)
```
"""


def my_sum(*args):
    print(type(args))
    print(args)
    return sum(args)


def test(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs.items())
    for k, v in kwargs.items():
        print(f"{k} -> {v}")


print(my_sum(1, 2, 3))
test(name="ldq", gender="male")


class Operations:
    def say_hi(self, name):
        print("Hi ", name)

    def default(self, arg):
        print("operation not supported")


if __name__ == "__main__":
    operations = Operations()
    command, arg = input(">").split()
    getattr(operations, command, operations.default)(arg)
