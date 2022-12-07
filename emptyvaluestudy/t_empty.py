# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/3 10:57
@Auth ： 仔仔
@File ：t_empty.py
"""


def main():
    t_bool()
    # t_not()
    pass


def t_bool():
    print(' bool(0)=>', bool(0))
    print(' bool('')=>', bool(''))
    print("bool('0')=>", bool('0'))  # True
    print(' bool([])=>', bool([]))
    print(' bool({})=>', bool({}))
    print(' bool(())=>', bool(()))
    print(' bool(None)=>', bool(None))
    print(' bool(set())=>', bool(set((1, 2))))

    pass


def t_not():
    # not其实就是逻辑非运算符，也就是其他语言中的感叹号
    # or 逻辑或运算符
    # and 逻辑与运算符
    tmp = 0
    if not tmp:
        print('not-数字0=>', False)
    print('数字0 is None=>', tmp is None)
    print('数字0 == 空字符串=>', tmp == '')
    print('False == 空字符串=>', False == '')
    print('[] == 空字符串=>', [] == '')
    print('{} == 空字符串=>', {} == '')
    print('() == 空字符串=>', () == '')
    print('----------')

    tmp = ''
    if not tmp:
        print('not-空字符串=>', False)

    tmp = []
    if not tmp:
        print('not-空list=>', False)

    tmp = {}
    if not tmp:
        print('not-空dict=>', False)

    tmp = ()
    if not tmp:
        print('not-空tuple=>', False)

    tmp = False
    if not tmp:
        print('not-布尔False=>', False)

    # python不认为字符串0是false
    tmp = '0'
    if not tmp:
        print("not-字符串'0'=>", False)


if __name__ == '__main__':
    main()
