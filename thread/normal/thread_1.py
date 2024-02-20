import threading


def task():
    print("Hello, World!\n")


if __name__ == "__main__":
    thread1 = threading.Thread(target=task)
    thread2 = threading.Thread(target=task)
    thread1.start()
    thread2.start()
