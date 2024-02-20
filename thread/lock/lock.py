import threading
import time

number = 0
lock = threading.Lock()


class MyThread(threading.Thread):

    def __init__(self, name, timeout: int):
        super().__init__()
        self.name = name
        self.timeout = timeout

    def run(self) -> None:
        time.sleep(2)
        global number
        for _i in range(100000):
            lock.acquire()  # 开锁，只允许当前线程访问共享的数据
            number += 1
            lock.release()  # 释放锁，允许其他线程访问共享数据

            # 可以使用with

    def run_with(self) -> None:
        time.sleep(2)
        global number
        for _i in range(100000):
            with lock:
                number += 1


if __name__ == "__main__":
    for i in range(1, 3):
        t = MyThread(str(i), 5)
        t.start()
        # t.join()

    # 给5秒钟让两个子线程执行完毕
    # time.sleep(5)
    # 确保两个子线程执行完毕
    print("活跃的线程个数：", threading.active_count())
    # 输出最终数值
    print("number: ", number)
