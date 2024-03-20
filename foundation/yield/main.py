# -*- coding: utf-8 -*-

"""
生成器：
    1.延迟操作，是指在需要的时候才产生结果，而不是立即产生结果

    Python有两种不同的方式提供生成器：
    1.生成器函数：常规函数定义，
    但是，使用yield语句而不是return语句返回结果。yield语句一次返回一个结果，
    在每个结果中间，挂起函数的状态，以便下次重它离开的地方继续执行。
    2.生成器表达式：类似于列表推导，
    但是，生成器返回按需产生结果的一个对象，而不是一次构建一个结果列表。

    生成器特点：
    1.自动实现迭代器协议
    2.状态挂起
    3.生成器只能遍历一次
"""


def func_main():
    func_t1()
    pass


# 方式一：生成器函数
def gen_squares(n):
    for i in range(n):
        yield i ** 2


# 方式二：使用普通函数
def gen_squares2(n):
    res = []
    for i in range(n):
        res.append(i * i)
    return res


# 方式三：生成器表达式
squares = (x ** 2 for x in range(5))
summ = sum(x ** 2 for x in range(4))


def func_t1():
    for item in gen_squares(5):
        print(item)

    print(next(squares))
    print(next(squares))
    print(next(squares))
    print(next(squares))


def func_t2():
    def func_a():
        yield "first in func_a!"
        yield from func_b()
        yield "second in func_a!"
        yield "third in func_a!"

    def func_b():
        yield "first in func_b!"
        yield "second in func_b!"
        yield "third in func_b!"

    iters = func_a()
    for i in iters:
        print(i)


def gen(n):
    for i in range(n):
        print("函数内部")
        yield i
        yield 22


if __name__ == '__main__':
    g = gen(5)
    print("g:", g)
    print(type(g))

    print("y:", next(g))
    print("y:", next(g))