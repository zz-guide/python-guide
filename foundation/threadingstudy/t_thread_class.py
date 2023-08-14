from threading import Thread
from time import sleep, ctime


class MyClass(object):

    @staticmethod
    def func_task(name, sec):
        print('---开始---', name, '时间', ctime())
        sleep(sec)
        print('***结束***', name, '时间', ctime())


def func_main():
    # 创建 Thread 实例
    t1 = Thread(target=MyClass.func_task, args=(1, 1))
    t2 = Thread(target=MyClass.func_task, args=(2, 2))

    # 启动线程运行
    t1.start()
    t2.start()

    # 等待所有线程执行完毕
    t1.join()  # join() 等待线程终止，要不然一直挂起
    t2.join()

    pass
