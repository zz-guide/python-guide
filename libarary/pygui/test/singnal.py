# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QObject, Signal, Slot


class CustomSignal(QObject):
    signal1 = Signal()  # 无参数的信号
    signal2 = Signal(int)  # 带一个参数（整数）的信号
    signal3 = Signal(int, str)  # 带两个参数（整数，字符串）的信号
    signal4 = Signal(list)  # 带一个参数（列表）的信号
    signal5 = Signal(dict)  # 带一个参数（字典）的信号
    signal6 = Signal([int, str], [str])  # 带（整数 字符串）或者（字符串）的信号

    def __init__(self, parent=None):
        super(CustomSignal, self).__init__(parent)

        # 信号与槽函数的链接
        self.signal1.connect(self.signal_call_1)
        self.signal2.connect(self.signal_call_2)
        self.signal3.connect(self.signal_call_3)
        self.signal4.connect(self.signal_call_4)
        self.signal5.connect(self.signal_call_5)
        self.signal6[int, str].connect(self.signal_call_6)
        self.signal6[str].connect(self.signal_call_7)

        # 信号发射
        self.signal1.emit()
        self.signal2.emit(1)
        self.signal3.emit(1, '第三个')
        self.signal4.emit([1, 2, 3, 4])
        self.signal5.emit({"name": 'JIA', 'age': '21'})
        self.signal6[int, str].emit(1, "第六")
        self.signal6[str].emit('第六')

    # 槽函数
    def signal_call_1(self):
        print("signal1 emit")

    def signal_call_2(self, val):
        print('signal2 emit,value:', val)

    def signal_call_3(self, val, text):
        print('signall3 emit,value:', val, text)

    def signal_call_4(self, val):
        print('signal4 emit,value:', val)

    def signal_call_5(self, val):
        print('signal5 emit,value', val)

    def signal_call_6(self, val, text):
        print('signal6 emit,value', val, text)

    def signal_call_7(self, val):
        print('signal6 overload emit', val)


if __name__ == '__main__':
    custom_signal = CustomSignal()
