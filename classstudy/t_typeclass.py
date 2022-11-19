def say(self):
    print("我要学 Python！")


# 使用 type() 函数创建类
# 其中 name 表示类的名称；bases 表示一个元组，其中存储的是该类的父类；dict 表示一个字典，用于表示类内定义的属性或者方法。
# 注意，Python 元组语法规定，当 (object,) 元组中只有一个元素时，最后的逗号（,）不能省略。
CLanguage = type("CLanguage", (object,), dict(say=say, name="C语言中文网"))
# 创建一个 CLanguage 实例对象
clangs = CLanguage()
# 调用 say() 方法和 name 属性
clangs.say()
print(clangs.name)

# MetaClass元类，本质也是一个类，但和普通类的用法不同，它可以对类内部的定义（包括类属性和类方法）进行动态的修改。可以这么说，使用元类的主要目的就是为了实现在创建类时，能够动态地改变类中定义的属性或者方法。
