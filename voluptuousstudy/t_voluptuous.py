# -*- coding: utf-8 -*-
"""
@Time ： 2022/12/3 15:34
@Auth ： 仔仔
@File ：t_voluptuous.py
"""
import datetime

from voluptuous import Schema, Required, All, Length, Range, Datetime
from voluptuous.error import MultipleInvalid, Invalid


def main():
    t()
    pass


def t():
    # 定义规则
    schema = Schema({
        # Required('username', msg='账号必填', default='xule'): All(
        #     str, Length(min=5, max=20, msg='账号长度在5-20之间')),
        # Required('age', msg='年龄必填', default=5): All(int, Range(min=10, max=150, msg='年龄必须大于10小于150')),
        Required('created_at', msg='开始时间必填', default=datetime.datetime.now()): All(str, Datetime()),
    })

    data = {}

    try:
        res = schema(data)
        print("通过校验:", res)
    except Invalid as e:
        print("校验失败:", type(e), e.msg)
    pass


if __name__ == '__main__':
    main()
