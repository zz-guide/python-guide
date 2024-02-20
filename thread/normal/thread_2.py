import threading


class MyThread(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print(f"[{self.name}]: Hello, World!\n")


if __name__ == "__main__":
    thread1 = MyThread("线程1")
    thread2 = MyThread("线程2")
    thread1.start()
    thread2.start()
