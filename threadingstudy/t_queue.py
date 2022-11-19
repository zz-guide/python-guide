# Queue 模块可以实现多生产者与多消费者队列，它可以实现多个线程之间的信息安全交换。

import threading, time
import queue

# 最多存入10个
q = queue.PriorityQueue(10)


def producer(name):
    ''' 生产者 '''
    count = 1
    while True:
        # 　生产袜子
        q.put("袜子 %s" % count)  # 将生产的袜子方法队列
        print(name, "---生产了袜子", count)
        count += 1
        time.sleep(0.2)


def consumer(name):
    """
    消费者
    """
    
    while True:
        print("%s ***卖掉了[%s]" % (name, q.get()))  # 消费生产的袜子
        time.sleep(1)
        q.task_done()  # 告知这个任务执行完了


# 生产线程
z = threading.Thread(target=producer, args=("张三",))
# 消费线程
l = threading.Thread(target=consumer, args=("李四",))
w = threading.Thread(target=consumer, args=("王五",))

# 执行线程
z.start()
l.start()
w.start()
