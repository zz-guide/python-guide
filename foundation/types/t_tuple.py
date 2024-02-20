def func_main():
    func_tuple()
    pass


def func_tuple():
    # Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    # 元组使用小括号 ( )，列表使用方括号 [ ]。
    # 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
    tup1 = ('Google', 'Runoob', 1997, 2000)
    # 元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
    tup2 = (50)
    # 不加逗号，类型为整型
    print(type(tup2))
    tup3 = (50,)
    # 加逗号，类型为元组
    print(type(tup3))
    # 元组不能直接修改，但是可以通过截取和组合产生新的元组，也可以直接进行赋值覆盖
    tup4 = ('r', 'u', 'n', 'o', 'o', 'b')
    # tup4[0] = 'g'  # 不支持修改元素， 'tuple' object does not support item assignment
    print(id(tup4))  # 查看内存地址
    tup4 = (6, 6, 6)
    print(id(tup4))  # 查看内存地址
    pass
