import time


class Student:
    name = ""
    age = 0
    __address = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return "%s %s" % (self.name, self.age)

    def __str__(self):
        return "asdasd"

    @staticmethod
    def show_time():
        now = time.strftime("%H:%M:%S", time.localtime())
        print(now)


def func_main():
    stu = Student("999", 20)
    print(stu)
    # stu.name = "许磊"
    # stu.age = 28
    print(stu.say())

    # 静态方法,可以使用实例调用，也可以使用类调用
    stu.show_time()

    Student.show_time()
