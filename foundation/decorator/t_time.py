import time
import threading


# 装饰器实际上就是一个内部函数
def execute_time(func):
    def inner():
        t_start = time.time()
        func()
        t_end = time.time()
        print(f"一共花费了{format(t_end - t_start)}秒时间")

    return inner


def func_main():
    def sleep_5s():
        time.sleep(5)
        print("%d秒结束了" % (5,))

    def sleep_6s():
        time.sleep(6)
        print("%d秒结束了" % (6,))

    sleep_5s = execute_time(sleep_5s)
    sleep_6s = execute_time(sleep_6s)

    t1 = threading.Thread(target=sleep_5s)
    t2 = threading.Thread(target=sleep_6s)
    t1.start()
    t2.start()
    pass
