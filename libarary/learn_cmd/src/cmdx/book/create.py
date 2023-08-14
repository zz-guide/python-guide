# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/5 22:57
@Auth ： 仔仔
@File ：create.py
"""
from cmd import Cmd

class CreateBookCmd(Cmd):
    def __init__(self):
        super().__init__()
        self.intro = '### 请依次输入图书名称,作者,类型,出版社。例如: 三体,xx,科幻,人民出版社'


    def preloop(self):
        pass


    def do_help(self, arg: str):
        print(self.intro)


    def do_q(self, argv):
        return True

    def default(self, line):  # 输入无效命令处理办法
        print('line:', line)
        print(u"没有这个命令")

