class Singleton(object):
    # 单例模式
    _instance = None

    def __new__(cls, *args, **kwargs):
        print("__new__ is called")
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, x, y):
        print("__init__ is called")
        self.name = x
        self.height = y


def func_main():
    p1 = Singleton("zhangsan", 180)
    print(p1)
    print(p1.name)
    p2 = Singleton("lishi", 175)
    print(p2)
    print(p2.name)
    print(p1.name)
