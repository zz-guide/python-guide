class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # python的类型标注并不是强类型的，为了方便编译器提示语法什么的，仍然可以运行
    def aaa(self) -> str:
        return True


def func_main():
    stu = Student("999", 20)
    print(stu.aaa())


# 类的实例，可以被外部直接导入
stu1 = Student('hah', 44)

if __name__ == '__main__':
    stu = Student('hah', 44)
    print(stu)
