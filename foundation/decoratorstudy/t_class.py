import time


def func_main():
    f1(2)
    pass


class Decorator:
    def __init__(self, func):
        self.func = func

    def defer_time(self, time_sec):
        print("开始延时")
        time.sleep(time_sec)
        print("延时结束了")

    def __call__(self, *args, **kwargs):
        self.defer_time(args[0])
        self.func()


@Decorator
def f1():
    print("延时之后我才开始执行")
