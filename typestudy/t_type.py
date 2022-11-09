def func_main():
    var_int = 1
    print("int类型", var_int, type(var_int), isinstance(var_int, int))
    var_float = 1.1
    print("float类型", var_float, type(var_float), isinstance(var_float, float))
    var_bool = True
    print("bool类型", var_bool, type(var_bool), isinstance(var_bool, bool))
    var_complex = 4 + 3j
    print("complex类型(复数)", var_complex, type(var_complex), isinstance(var_complex, complex))
    var_string1 = '许磊'
    var_string2 = "许磊"
    var_string3 = """许磊"""
    print("string类型", var_string1, type(var_string1), isinstance(var_string1, str))
    print("string类型", var_string2, type(var_string2), isinstance(var_string2, str))
    print("string类型", var_string3, type(var_string3), isinstance(var_string3, str))
    var_list = ['abcd', 786, 2.23, 'runoob', 70.2]
    print("list类型(类似php的数组)", var_list, type(var_list), isinstance(var_list, list))
    var_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
    print("tuple类型(无法修改)", var_tuple, type(var_tuple), isinstance(var_tuple, tuple))
    var_set = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 123}
    print("set类型", var_set, type(var_set), isinstance(var_set, set))
    var_dict = {"name": "许磊", "address": "地址"}
    print("dict类型(本质是map)", var_dict, type(var_dict), isinstance(var_dict, dict))


def fun_mark():
    """
    # type()不会认为子类是一种父类类型。
    # isinstance()会认为子类是一种父类类型。
    # bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
    # 在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
    """
