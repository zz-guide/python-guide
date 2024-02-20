import threading
import time


class MyThread(threading.Thread):

    def __init__(self, name, timeout: int):
        super().__init__()
        self.name = name
        self.timeout = timeout

    def run(self) -> None:
        print(f"[{self.name}]: 休眠中...\n")
        time.sleep(self.timeout)
        print(f"[{self.name}]: 结束...\n")


if __name__ == "__main__":
    thread1 = MyThread("线程1", 5)
    thread2 = MyThread("线程2", 7)
    thread1.start()
    thread2.start()
    print("活跃的线程数:", threading.active_count())

