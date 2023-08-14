from typing import Dict, List


def func_main():
    t_base_type()
    pass


def t_base_type():
    # 结论：dict,list在函数内部修改可能会影响外部实参的值，所以建议默认值不要设置为list[],dict{}
    a = 123
    b = ''
    c = (1, 'xulei')
    d = True
    e = None
    f = [1, 2, 3]
    g = {'a': 'a', 'b': 'b'}
    t(a, b, c, d, e, f, g)
    print('---------------')
    print('a:', type(a), a)
    print('b:', type(b), b)
    print('c:', type(c), c)
    print('e:', type(e), e)
    print('f:', type(f), f)
    print('g:', type(g), g)
    pass


def t(a=123, b='', c=(1, 'xulei'), d=True, e=None, f: List[int] = [], g: Dict[str, str] = {}):
    print('a-:', type(a), a)
    print('b-:', type(b), b)
    print('c-:', type(c), c)
    print('e-:', type(e), e)
    print('f-:', type(f), f)
    print('g-:', type(g), g)
    a = 456
    b = 'xulei'
    c = (1, 2, 3)
    d = False
    e = [1, 2, 3]
    # 直接赋值不会影响外边，但是append方法会影响外边的值
    f.append(6)
    # 直接覆盖dict不会影响外边的值，但是修改会影响
    g['a'] = 'sadasd'


if __name__ == '__main__':
    func_main()
