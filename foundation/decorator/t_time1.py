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


def mylog(func):
    print("mylog函数开始了111")

    # 装饰器带参数的写法
    def inner(*args, **kwargs):
        print("start")
        func()
        print("end")

    print("mylog函数开始了2222")
    return inner


@mylog
@execute_time
def sleep_5s():
    time.sleep(5)
    print("%d秒结束了" % (5,))


# 语法糖
@mylog
@execute_time
def sleep_6s():
    time.sleep(6)
    print("%d秒结束了" % (6,))


# 多个装饰器执行顺序，先执行execute_time外部代码，其次mylog外部代码，其次mylog内部函数代码，其次execute_time内部函数代码

def func_main():
    # t1 = threading.Thread(target=sleep_5s)
    # t2 = threading.Thread(target=sleep_6s)
    # t1.start()
    # t2.start()
    pass
