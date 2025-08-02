from time import sleep
from celery import Celery

app = Celery(
    'mre',
    backend="redis://:foobar@127.0.0.1:1432/0",
    broker="redis://:foobar@127.0.0.1:1432/1"
)

@app.task
def noop() -> None:
    pass