class AAA:
    def __init__(self):
        self.name = "asdasd"


class Student:
    aaa = AAA()


if __name__ == '__main__':
    print(Student.aaa.name)
