# -*- coding: utf-8 -*-

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