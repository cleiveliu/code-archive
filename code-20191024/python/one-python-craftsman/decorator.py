

import time
import functools


class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"wait for {self.duration} seconds ...")
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        return self.func(*args, **kwargs)


def delay(duration=2):
    return functools.partial(DelayFunc, duration)


@delay(duration=3)
def add(a, b):
    return a+b


print(add(1, 10))

print(add.eager_call(10, 100))


print(locals())
