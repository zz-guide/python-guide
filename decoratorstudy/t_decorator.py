def func_main():
    stu = Student()
    print(stu.read_only_property())
    # 调用不需要加括号
    print(stu.age)
    pass


class Student:
    # 不含@property 定义只读属性
    def read_only_property(self):
        return 14

    @property
    def age(self):
        return 2014 - self._birth

    # 对 @ property只定义getter方法，不定义setter方法就是一个只读属性.
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @staticmethod
    def ppp():
        return "@staticmethod静态方法"

    @classmethod  # 第一个参数类自身,用来实现类的重载
    def ttt(cls):
        cls.ppp()
