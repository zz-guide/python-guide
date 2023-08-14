# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/5 20:18
@Auth ： 仔仔
@File ：main.py
"""
from cmd import Cmd

from src.cmdx.book import CreateBookCmd


def print_log(argv):
    print('argv:', argv, type(argv))

class RootCmd(Cmd):
    """
    cmd命令行交互程序
    """
    def __init__(self):
        super().__init__()
        # 自定义交互式提示字符串
        self.prompt = "Cmd_xulei>"

        # 自定义我们的欢迎语
        self.intro = '欢迎使用图书管理系统V1.0'

    def preloop(self):
        print('==============================================================')
        print('1.添加图书信息')
        print('2.导入图书信息')
        print('3.删除图书信息')
        print('4.查询所有图书信息')
        print('5.查询指定图书信息')
        print('6.查询人民邮电出版社出版的图书信息')
        print('7.统计人民邮电出版社出版的图书数量')
        print('8.导出数据')
        print('9.退出系统')
        print('==============================================================')

    def do_help(self, arg: str):
        print(self.intro)

    def do_create(self, argv):
        create = CreateBookCmd()
        create.prompt = self.prompt + ':create>>>'
        create.cmdloop()

    def help_create(self):
        print("xxxxxxxxxx")

    # 当输入exit会自动调用该函数，返回True退出loop
    def do_exit(self, argv):
        return True

    def help_exit(self):
        print("退出系统")

    # 自动补全命令的钩子函数,只能在linux下使用
    def completedefault(self, text, line, begidx, endidx):
        print(text, line, begidx, endidx)
        if not text:  # 列出可选参数
            completions = ['server', 'trader', 'old_account', 'new_account', 'run']
            return completions
        else:
            completions = ['server', 'trader', 'old_account', 'new_account', 'run']  # 补全参数
            return [i for i in completions if i.startswith(text)]

    # 当输入空行时调用该方法
    def emptyline(self):
        print( 'please input command!')

    def default(self, line):  # 输入无效命令处理办法
        print('line:', line)
        print(u"没有这个命令")



if __name__ == '__main__':
    # noinspection PyBroadException
    try:
        root_cmd = RootCmd()
        root_cmd.cmdloop()
    except:
        exit()

