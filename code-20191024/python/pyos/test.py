from pyos2 import Scheduler

def foo():
    for _ in range(10):
        print("I am foo")
        yield

def bar():
    for _ in range(15):
        print("I am bar")
        yield

sched = Scheduler()

sched.new(foo())
sched.new(bar())
sched.mainloop()