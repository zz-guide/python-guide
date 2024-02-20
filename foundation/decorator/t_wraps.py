import time
import threading
from functools import wraps


def mylog(func):
    print("mylog函数开始了")

    # 装饰器带参数的写法
    @wraps(func)
    def inner(*args, **kwargs):
        print("start")
        func()
        print("end")

    return inner


@mylog
def sleep_5s():
    time.sleep(5)
    print("%d秒结束了" % (5,))


# 语法糖
@mylog
def sleep_6s():
    time.sleep(6)
    print("%d秒结束了" % (6,))


# 多个装饰器执行顺序，先执行execute_time外部代码，其次mylog外部代码，其次mylog内部函数代码，其次execute_time内部函数代码

def func_main():
    t1 = threading.Thread(target=sleep_5s)
    t2 = threading.Thread(target=sleep_6s)
    t1.start()
    t2.start()
    pass
