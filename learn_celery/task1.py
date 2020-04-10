import time
from learn_celery import app


@app.task
def add(x, y):
    time.sleep(5)
    return x + y
