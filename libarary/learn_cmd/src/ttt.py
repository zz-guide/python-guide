# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/5 22:51
@Auth ： 仔仔
@File ：ttt.py
"""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:   craftsman2020

from __future__ import print_function
import sys
import cmd

VERSION = int(sys.version_info[0])
TRADERS = {'a': 'aaa', 'b': 'bbb'}
RUN_DICT = {}

SFTP_ACCOUNTS = {
    'jack': '123456',
    'aaa': '666666',
    'bbb': '888888',
}

SERVERS = {
    'server_123': ['101.122.122.122', 55555, 'jack', SFTP_ACCOUNTS['jack'], ['hahaha', 'wowowo'], []],
}


class ServerCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        cmd.Cmd.intro = "### Please input the name of server, Example: server_123"

    def default(self, server):
        print('server = ', server)
        if server in SERVERS:
            print(SERVERS[server])
            RUN_DICT['server'] = server
            return True
        else:
            print(u'### 请检查server信息是否正确! server参数可配置的范围:\n{}'.format([i for i in SERVERS]))
            return False

    def preloop(self):
        print("### Welcome to Server module")

    def postloop(self):
        print("### Exit Server module")

    def do_q(self, line):
        return True

    def help_q(self):
        print("### 返回主循环")


class TraderCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        cmd.Cmd.intro = "### Please input the abbreviation of Trader's name, Example: a b"

    def default(self, trader):
        traders = trader.split()
        print('traders = ', traders)
        traders = [i.strip() for i in traders]
        traders_dic = dict()
        for t in traders:
            if t in TRADERS:
                traders_dic[t] = TRADERS[t]
            else:
                print(u'### 请检查trader信息是否正确! trader参数可配置的范围: \n{}'.format(TRADERS))
                return False
        print(traders_dic)
        RUN_DICT['traders'] = traders_dic
        return True

    def preloop(self):
        print("### Welcome to Trader module")

    def postloop(self):
        print("### Exit Trader module")

    def do_q(self, line):
        return True

    def help_q(self):
        print("### 返回主循环")


class OldAccountCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        cmd.Cmd.intro = "### Please input the old account, Example: hahaha"

    def default(self, old_account):
        print('old_account = ', old_account)
        if old_account in SERVERS[RUN_DICT['server']][-2]:
            RUN_DICT['old_account'] = old_account
            return True
        else:
            print(u'### 请检查old_account信息是否正确! old_account参数可配置的范围: \n{}'.format(
                SERVERS[RUN_DICT['server']][-2]))
            return False

    def preloop(self):
        print("### Welcome to OldAccount module")

    def postloop(self):
        print("### Exit OldAccount module")

    def do_q(self, line):
        return True

    def help_q(self):
        print("### 返回主循环")


class NewAccountCmd(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        cmd.Cmd.intro = "### Please input new accounts:"

    def default(self, new_account):
        new_accounts = new_account.split()
        print('new_accounts = ', new_accounts)
        new_accounts = [i.strip() for i in new_accounts]
        RUN_DICT['new_accounts'] = new_accounts
        return True

    def preloop(self):
        print("### Welcome to NewAccount module")

    def postloop(self):
        print("### Exit NewAccount module")

    def do_q(self, line):  # 这个的do_exit和do_quit并没有什么区别
        return True

    def help_q(self):
        print("### 返回主循环")


class MyShell(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "main>>>"
        self.intro = """### Start deploying >>> """
        self.doc_header = "Commands"
        self.doc_leader = 'this is leader'  # 其他两个misc_header undoc_header是无效的

    def do_help(self, line):
        print('==============================================================')
        print('module: { server, trader, old_account, new_account, run, exit}')
        print('--------------------------------------------------------------')
        print(u'server: 配置服务器参数, do_he只能输入SERVERS中的服务器名称')
        print(u'trader: 配置trader参数, 只能输入TRADERS中的trader名称')
        print(u'old_account: 模板账户, 只能输入SERVERS中的模板账户名称')
        print(u'new_account: 新账户, 新上线的账户名称')
        print(u'run: 根据配置的参数, 开始部署')
        print(u'exit: 退出交互器')
        print('==============================================================')

    def preloop(self):
        self.do_help('')
        print('******************************************************')
        print(u"1、进入各模块配置参数: server, trader, old, new")
        print(u"2、核对参数无误后, run")
        print('******************************************************')

    def postloop(self):
        print(u"程序运行结束!")

    def do_server(self, line):
        s = ServerCmd()  # 嵌套新的解释器
        s.prompt = self.prompt + ':Server>>>'
        s.cmdloop()

    def do_trader(self, line):
        t = TraderCmd()  # 嵌套新的解释器
        t.prompt = self.prompt + ':Trader>>>'
        t.cmdloop()

    def help_server(self):
        print(u"进入Server模块设置服务器配置项")

    def help_trader(self):
        print(u"进入Trader模块设置trader配置项")

    def do_old(self, old_account):
        o = OldAccountCmd()  # 嵌套新的解释器
        o.prompt = self.prompt + ':OldAccount>>>'
        o.cmdloop()

    def help_old(self):
        print(u"进入OldAccount模块, 设置OldAccount配置项")

    def do_new(self, new_account):
        n = NewAccountCmd()  # 嵌套新的解释器
        n.prompt = self.prompt + ':NewAccount>>>'
        n.cmdloop()

    def help_new(self):
        print(u"进入NewAccount模块, 设置NewAccount配置项")

    def do_run(self, line):
        print('RUN_DICT = ', RUN_DICT)
        deploy()

    def help_run(self):
        print(u"参数配置完成后, 开始运行...")

    # options是自动补全的 [python2 windows会自动补全]
    def completedefault(self, text, line, begidx, endidx):
        if not text:  # 列出可选参数
            completions = ['server', 'trader', 'old_account', 'new_account', 'run']
            return completions
        else:
            completions = ['server', 'trader', 'old_account', 'new_account', 'run']  # 补全参数
            return [i for i in completions if i.startswith(text)]

    def do_exit(self, line):
        print("Exit Program!")
        # sys.exit()不需要自己退出的,会有问题
        return True

    def help_exit(self):
        print(u"退出交互器")

    def emptyline(self):
        pass

    def default(self, line):
        print(u"没有这个命令")

    def do_EOF(self, line):
        return True


def deploy():
    # python2
    print("test hello world!")




if __name__ == '__main__':
    MyShell().cmdloop()
