# Event 事件锁对象
# 用于线程间通信，即程序中的其一个线程需要通过判断某个线程的状态来确定自己下一步的操作，就用到了event()对象。event()对象有个状态值，他的默认值为 Flase，即遇到 event() 对象就阻塞线程的执行。
# 观察结果会发现，t1线程运行的func函数需要等到connect函数运行event.set()后才继续执行之后的操作。

import threading

event = threading.Event()


def func():
    print('等待服务响应...')
    event.wait()  # 等待事件发生
    print('连接到服务')


def connect():
    print('成功启动服务')
    event.set()


t1 = threading.Thread(target=func, args=())
t2 = threading.Thread(target=connect, args=())

t1.start()
t2.start()
