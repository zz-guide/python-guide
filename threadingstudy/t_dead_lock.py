import threading
import time

# 生成一个锁对象
lock1 = threading.Lock()
lock2 = threading.Lock()


# 多线程最怕的是遇到死锁，两个或两个以上的线程在执行时，因争夺资源被相互锁住而相互等待。
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self) -> None:
        self.fun_A()
        self.fun_B()

    def fun_A(self):
        lock1.acquire()
        print('A_1 加锁', end='\t')
        lock2.acquire()
        print('A-2 加锁', end='\t')
        time.sleep(0.1)
        lock2.release()
        print('A-2 释放', end='\t')
        lock1.release()
        print('A-1 释放')

    def fun_B(self):
        lock2.acquire()
        print('B-1 加锁', end='\t')
        lock1.acquire()
        print('B-2 加锁', end='\t')
        time.sleep(0.1)
        lock1.release()
        print('B-1 释放', end='\t')
        lock2.release()
        print('B-2 释放')


def func_main():
    # 需要四个以上线程，才会出现死锁现象
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
    pass
