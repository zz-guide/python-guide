import threading
import time
import random

# 同步两个不同线程，信号量被初始化0
semaphore = threading.Semaphore(0)


def consumer():
    print("-----等待producer运行------")
    semaphore.acquire()  # 获取资源，信号量为0被挂起，等待信号量释放
    print("----consumer 结束----- 编号: %s" % item)


def producer():
    global item  # 全局变量
    time.sleep(3)
    item = random.randint(0, 100)  # 随机编号
    print("producer运行编号: %s" % item)
    semaphore.release()


"""
信号量被初始化为0，目的是同步两个或多个线程。线程必须并行运行，所以需要信号量同步。这种运用场景有时会用到，比较难理解，多运行示例仔细观察打印结果。

拓展：

信号量的一个特殊用法是互斥量。互斥量是初始值为1的信号量，可以实现数据、资源的互斥访问。

信号量在在多线程的编程语言中应用很广，他也有可能造成死锁的情况。例如，有一个线程t1，先等待信号量s1，然后等待信号量s2，而线程t2会先等待信号量s2，然后再等待信号量s1，这样就会发生死锁，导致t1等待s2，但是t2在等待s1。


"""


def func_main():
    for i in range(0, 4):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print("程序终止")
