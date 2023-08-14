import time

"""
结论：
    1.直接定义在类中的变量是类变量，可以被类调用，也可以被实例调用。
    2.可以修改类变量的值，会作用到所有的实例对象。
    3.不能使用实例去修改类变量，这样只会产生一个新的实例属性。
    4.可以动态的为类添加类变量。
    5.实例变量和类变量可以同名，但这种情况下使用类对象将无法调用类变量，它会首选实例变量，这也是不推荐“类变量使用对象名调用”的原因。
    6.通过某个对象修改实例变量的值，不会影响类的其它实例化对象，更不会影响同名的类变量
    7.Python 中允许使用类名直接调用实例方法，但必须手动为该方法的第一个 self 参数传递参数，这种调用方法的方式被称为“非绑定方法”。
        class CLanguage:
            def info(self):
                print("我正在学 Python")
        clang = CLanguage()
        #通过类名直接调用实例方法
        CLanguage.info(clang)

"""


class Student:
    # 类变量
    name = ""
    age = 0
    __address = None

    def __init__(self, name, age):
        # 实例的成员属性
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
