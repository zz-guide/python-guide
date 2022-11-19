# 重入锁(递归锁) threading.RLock()
# 为了支持同一个线程中多次请求同一资源，Python 提供了可重入锁(RLock)。这个RLock内部维护着一个锁(Lock)和一个计数器(counter)变量，counter 记录了acquire 的次数，从而使得资源可以被多次acquire。直到一个线程所有 acquire都被release(计数器counter变为0)，其他的线程才能获得资源。


import time
import threading

# 生成一个递归对象
Rlock = threading.RLock()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.fun_A()
        self.fun_B()

    def fun_A(self):
        Rlock.acquire()
        print('A加锁1', end='\t')
        Rlock.acquire()
        print('A加锁2', end='\t')
        time.sleep(0.2)
        Rlock.release()
        print('A释放1', end='\t')
        Rlock.release()
        print('A释放2')

    def fun_B(self):
        Rlock.acquire()
        print('B加锁1', end='\t')
        Rlock.acquire()
        print('B加锁2', end='\t')
        time.sleep(3)
        Rlock.release()
        print('B释放1', end='\t')
        Rlock.release()
        print('B释放2')


def func_main():
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
