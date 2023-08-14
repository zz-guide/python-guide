def func_main():
    names = ["张三", "李四", "王五", "赵六"]
    # for in 中无法获取迭代索引
    for item in names:
        print(item)

    # 仍然可以访问
    # print(item)

    # 通过range获取索引
    for i in range(len(names)):
        print(i, names[i])
