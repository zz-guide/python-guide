from typing import Dict, List

"""
结论：
    1. python的参数定义以后，不加默认值就是必传，不传执行报错
    2. python的参数类型只能做到提示，不是强严格，传类型不一致的值也可以
"""


def func_main():
    t1()
    pass


def t1():
    # custom()  # 什么都不传，报错
    # custom(None)
    # custom('ss')
    pass


def custom(p: int):
    print('type(p):', type(p))
    print('p is None:', p is None)
    print('p:', p)
    print('######')


if __name__ == '__main__':
    func_main()
