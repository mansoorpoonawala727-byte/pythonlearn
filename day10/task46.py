def log_lines():
    yield "INFO: system start"
    yield "WARNING: high memory"
    yield "ERROR: intrusion detected"
logs = log_lines()
print(next(logs))
print(next(logs))
print(next(logs))