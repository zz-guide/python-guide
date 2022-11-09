# 类的继承
class People:
    name = ""  # public 可以继承
    __address = None  # private 不可继承
    _address = None  # protected 可以继承

    def __init__(self, name):
        self.name = name

    def say(self):
        return "%s" % self.name


class Animal:
    name = ""

    def __init__(self, name):
        self.name = name

    def say(self):
        return "%s" % self.name


# 多继承，冲突的成员优先继承写在前边的

class Dog(People, Animal):
    def say(self):
        return "狗 %s" % self.name


def func_main():
    animal = Animal("动物")
    print(animal.say())

    dog = Dog("狗")
    print(dog.say())
