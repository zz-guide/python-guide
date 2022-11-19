import operator


def func_main():
    func_list1()
    pass


def func_list1():
    # 列表能存储不同类型数据，类似php的数组
    l = ['字符串', 123, True]
    # 通过索引值访问列表数据
    print(l[0])
    print(l[1])
    # -1表示从末尾访问
    print(l[-1])
    print(l[-2])
    print(l)
    print('-------------')
    # 添加元素
    l.append(567)
    print(l)
    # del语句删除元素
    del l[0]
    print(l)
    print('-------------')
    # +组合列表
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(l1 + l2)
    # in 判断元素是否存在列表,不像PHP那样数字和字符串是互等的
    l3 = [1, 2, 3]
    print('3' in l3)
    # 列表的比较需要引入operator模块
    a = [1, 2]
    b = [2, 3]
    c = [2, 3]
    print("operator.eq(a,b): ", operator.eq(a, b))
    print("operator.eq(c,b): ", operator.eq(c, b))
    pass


def func_list2():
    pass
