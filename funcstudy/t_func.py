def func_main():
    # 测试 *

    # func_args("许磊", 123, [1, 2, 3])
    # func_args(*["许磊", 123, [1, 2]])
    # func_args(1, 2, 3, 4, 5, 6, 7)
    func_args2(1, 2, c=3, d=4, e=5, f=6, g=7)
    pass


def func_args(x, y, *args):
    # *args保存多余变量，保存方式为元组
    print("*args:", args, type(args))
    # tuple不能越界访问，tuple index out of range
    # print(args[0], args[1], args[2], args[3])

    # 传实参的时候，可以传入一个list,前边加个*可以自动拆解为tuple
    print("x=", x)
    print("y=", y)
    print("args=", args)
    pass


def func_args2(x, y, **kwargs):
    # **kwargs保存带有变量名的多余变量，保存方式为字典。
    print("x=", x)
    print("y=", y)
    print("kwargs=", kwargs, type(kwargs))
    for k, v in kwargs.items():
        print(k, v)
    pass
