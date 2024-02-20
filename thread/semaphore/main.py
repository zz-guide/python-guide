import threading
import time

number = 0
# 同时运行的线程数
semaphore = threading.BoundedSemaphore(3)


class MyThread(threading.Thread):

    def __init__(self, n):
        self.n = n
        super().__init__()

    def run(self) -> None:
        semaphore.acquire()
        for _i in range(100):
            _count = threading.active_count() - 1
            print(f"线程-{self.n}", f"当前活跃的子线程个数：{_count}")
            time.sleep(1)
        semaphore.release()


if __name__ == "__main__":
    for i in range(1, 10):
        t = MyThread(i)
        t.start()
