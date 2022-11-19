def func_main():
    func_open_file()
    pass


def func_open_file():
    # 打开一个文件
    # 参数说明:
    #
    # file: 必需，文件路径（相对或者绝对路径）。
    # mode: 可选，文件打开模式 # 查看 https://www.runoob.com/python3/python3-file-methods.html
    # buffering: 设置缓冲
    # encoding: 一般使用utf8
    # errors: 报错级别
    # newline: 区分换行符
    # closefd: 传入的file参数类型
    # opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
    with open('./ttt.txt', 'w') as file:
        print('打开文件成功')
        file.write('你好啊')
        file.close()

    print('成功')
    pass
