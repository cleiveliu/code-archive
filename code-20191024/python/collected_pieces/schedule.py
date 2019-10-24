from collections import deque


def count_down(n):
    while n > 0:
        print("T-minus ", n)
        yield
        n -= 1
    print("minus off")


def count_up(n):
    cur = 0
    while cur < n:
        print("now is", cur)
        yield
        cur += 1


class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def add_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self.add_task(task)
            except StopIteration:
                pass


# Example use
sched = TaskScheduler()
sched.add_task(count_down(10))
sched.add_task(count_down(5))
sched.add_task(count_up(15))
sched.run()