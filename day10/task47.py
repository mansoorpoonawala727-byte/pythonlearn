class LogIterator:
    def __init__(self, logs):
        self.logs = logs
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.logs):
            raise StopIteration
        log = self.logs[self.index]
        self.index += 1
        return log
logs = ["INFO: system start", "WARNING: high memory", "ERROR: intrusion detected"]
iterator = LogIterator(logs)
for log in iterator:
    print(log)    