from typing import Dict, List


def func_main():
    t_default()
    pass


def t_default():
    # 结论：类型注解不影响实际运行效果，只针对IDE和编译器优化
    # 建议，list和dict默认值为 List[str] = None,Dict[str, int] = None
    # 内部进行if None的判断
    f1 = [1, 2, 3]
    f1 = 123
    print(f)
    g = {'a': 'a', 'b': 'b'}
    t(f1, g)
    print('---------------')
    print('f:', type(f), f)
    print('g:', type(g), g)
    pass


def t(f=None, g: Dict[str, str] = {}):
    print('f-:', type(f), f)
    print('g-:', type(g), g)


if __name__ == '__main__':
    func_main()
