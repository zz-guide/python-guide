# 信号量(Semaphore)
# 信号量是一个内部数据，它有一个内置的计数器，它标明当前的共享资源可以有多少线程同时读取。

import time
import threading
import random

# 创建信号量对象，信号量设置为3，需要有3个线程才启动
semaphore = threading.Semaphore(3)


def func():
    if semaphore.acquire():  # 获取信号 -1
        print(threading.currentThread().getName() + '获得信号量')
        time.sleep(random.randint(1, 5))
        semaphore.release()  # 释放信号 +1


for i in range(10):
    t1 = threading.Thread(target=func)
    t1.start()
