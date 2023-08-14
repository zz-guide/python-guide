def func_main():
    # 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。
    # func_list_deduction()
    # func_dict_deduction()
    # func_set_deduction()
    func_tuple_deduction()
    pass


def func_list_deduction():
    # list 推导式
    # [表达式 for 变量 in 列表]
    # [out_exp_res for out_exp in input_list]
    #
    # 或者
    #
    # [表达式 for 变量 in 列表 if 条件]
    # [out_exp_res for out_exp in input_list if condition]
    names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
    new_names = [name.upper() for name in names if len(name) > 3]
    print(new_names)
    pass


def func_dict_deduction():
    # dict 推导式
    # { key_expr: value_expr for value in collection }
    #
    # 或
    #
    # { key_expr: value_expr for value in collection if condition }
    listdemo = ['Google', 'Runoob', 'Taobao']
    # 将列表中各字符串值为键，各字符串的长度为值，组成键值对
    newdict = {key: len(key) for key in listdemo}
    print(newdict)
    pass


def func_set_deduction():
    # set 推导式
    # { expression for item in Sequence }
    # 或
    # { expression for item in Sequence if conditional }
    setnew = {i ** 2 for i in (1, 2, 3)}
    print(setnew)
    pass


def func_tuple_deduction():
    # tuple 推导式
    # 元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
    # (expression for item in Sequence )
    # 或
    # (expression for item in Sequence if conditional )
    a = (x for x in range(1, 10))
    print(a)  # 元组推导式返回的结果是一个生成器对象。
    print(tuple(a))  # 使用 tuple() 函数，可以直接将生成器对象转换成元组
    pass
