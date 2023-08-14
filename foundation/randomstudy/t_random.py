import random


def func_main():
    func_random()
    pass


def func_random():
    # 设置随机数种子
    # random.seed(10, 2)
    # 生成随机数
    print(random.random())
    # random.seed("asd", 2)
    print(random.randint(0, 10))
    # seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。
    pass
