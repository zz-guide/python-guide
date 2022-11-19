from threading import Thread
from time import sleep, ctime


def func_task(name, sec):
    print('---开始---', name, '时间', ctime())
    sleep(sec)  # sleep会导致线程切换
    print('***结束***', name, '时间', ctime())


def func_main():
    # 创建 Thread 实例
    t1 = Thread(target=func_task, args=('第一个线程', 1))
    t2 = Thread(target=func_task, args=('第二个线程', 2))

    # 启动线程运行
    t1.start()
    t2.start()

    # 等待所有线程执行完毕
    # join() 等待线程终止，要不然一直挂起
    t1.join()
    t2.join()

    pass
