def func_main():
    func_dict()
    pass


def func_dict():
    # 字典是另一种可变容器模型，且可存储任意类型对象。
    # 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,
    # 类比go语言的Map
    # 键必须是唯一的，但值则不必。
    # 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。

    # # 使用大括号 {} 来创建空字典
    emptyDict = {}
    emptyDict = dict()
    print(emptyDict)

    tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
    del tinydict['Name']  # 删除键 'Name'
    # tinydict.clear()  # 清空字典
    # del tinydict  # 删除字典 会报错
    # print(tinydict)
    # print("tinydict['Age']: ", tinydict['Age'])
    # print("tinydict['School']: ", tinydict['School'])

    # dict新版本是有序的，插入和遍历的顺序一致，以前是不一致的
    pass
