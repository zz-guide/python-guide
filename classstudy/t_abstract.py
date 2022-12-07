import abc
from abc import ABC


def func_main():
    t_abstract()
    pass


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        pass


class Dog(Animal):
    # Can't instantiate abstract class Dog with abstract methods say
    # 不实现抽象方法，类名会有波浪线，运行报错
    def say(self):
        pass

    def hh(self):
        pass


def t_abstract():
    dog = Dog()
    dog.hh()
