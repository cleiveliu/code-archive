class Task:
    taskid = 0
    def __init__(self,target):
        Task.taskid += 1
        self.tid = Task.taskid # task id
        self.target = target   # target coroutine
        self.send_val = None   # value to send
    def run(self):
        return self.target.send(self.send_val)