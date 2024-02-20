from datetime import datetime
from threading import Timer
import time


def timed_task():
    _timer = Timer(1, task)
    _timer.start()


# 定时任务
def task():
    print("子线程:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    timed_task()
    while True:
        print("主线程:", time.time())
        time.sleep(3)
