# Lock 同步锁(原语锁）

# 我们一般使用获得锁(加锁)和释放锁(解锁)函数来控制锁的两种状态“锁定”和“未锁定”。
# 一般只要在公共操作前加上加锁和解锁的操作即可。

import time
import threading

# 生成一个锁对象
lock = threading.Lock()
num = 100
l = []


def func():
    global num  # 全局变量
    lock.acquire()  # 获得锁，加锁
    num1 = num
    time.sleep(0.1)
    num = num1 - 1
    lock.release()  # 释放锁，解锁
    time.sleep(2)


def func_main():
    # 注释掉锁和使用锁，返回的结果不同

    # 先统一创建线程，然后加到列表
    for i in range(100):  # 开启100个线程
        t = threading.Thread(target=func, args=())
        t.start()
        l.append(t)

    # 等待所有线程运行结束
    for i in l:
        i.join()

    print(num)
    pass
