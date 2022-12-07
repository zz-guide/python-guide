# Python中requirements.txt的生成

    requirements.txt 是Python项目中包含的一个文件，
    作用：用于记录所有依赖包及其精确的版本号，以便新环境使用。

    在原来项目中生成requirements.txt文件 Terminal中执行 pip freeze >requirements.txt
    则项目中生成该新文件

    在新项目中安装 requirements.txt文件 Terminal中执行 pip install - r requirements.txt

# __all__

    all 暴露接口
    1.当我们向文件导入某个模块时，导入的是该模块中那些名称不以下划线（单下划线“_”或者双下划线“__”）开头的变量、函数和类。因此，如果我们不想模块文件中的某个成员被引入到其它文件中使用，可以在其名称前添加下划线。
    2.还可以借助模块提供的__all__ 变量，该变量的值是一个列表，存储的是当前模块中一些成员（变量、函数或者类）的名称。通过在模块文件中设置__all__变量，当其它文件以“from 模块名 import *”的形式导入该模块时，该文件中只能使用__all__ 列表中指定的成员。__all__也是对于模块公开接口的一种约定，比起下划线，__all__提供了暴露接口用的“白名单”。
    注意：
    __all__变量只在以from 模块名 import *形式导入模块时起作用，而以其他形式，如import 模块名、from 模块名 import 成员时都不起作用。
    代码中当然是不提倡用 from xxx import * 的写法的，一般只用在临时代码如console调试中，这种时候如果没有定义__all__，会将模块中非下划线开头的所有成员都导入当前命名空间中，可能弄脏当前命名空间。
    __all__应该是list 类型的。
    不应该动态生成__all__，比如使用列表解析式。
    __all__的位置：按照 PEP8 建议的风格，__all__应该写在所有 import 语句下面，和函数、常量等模块成员定义的上面

# 装饰器

    python中的装饰器(decorator)一般采用语法糖的形式，是一种语法格式。比如：@classmethod，@staticmethod，@property，@xxx.setter，@wraps()，@func_name等都是python中的装饰器。
    装饰器，装饰的对象是函数或者方法。各种装饰器的作用都是一样的：改变被装饰函数或者方法的功能，性质。
    下面主要讲解@wraps()，@func_name，类装饰器这两种装饰器。
    1.第一大特性是，能把被装饰的函数替换成其他函数。
    2.第二个特性是，装饰器在加载模块时立即执行。

# 经典类和新式类

    class A(object):
    pass    # 新式类

    class A:
        pass   # 经典类 :在多继承中遵循深度优先
               # 经典类中没有super和mro方法

# python多线程

    全局解释器锁（GIL）
    只有CPython解释器有这个概念。
    Python中，每个线程的执行方式：
    1.获取GIL
    2.执行代码直到sleep或python解释器将其挂起。
    3.释放GIL因此，我们可以把GIL看作是“许可证”，一个线程若想要执行，必须先拿到GIL。
    并且在一个python进程中，GIL只有一个。拿不到“许可证”的线程，就不能执行。这就导致了在Python进程中，
    即使有多个线程，同一时间也是仅有一个线程在执行。所以，Python中的多线程是假的多线程。
    
    计算密集型任务：任务包含大量计算，消耗大量CPU资源。

    IO密集型任务：任务包含频繁的、持续的网络IO和磁盘IO。
    这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成。
    对于计算密集型的任务，多线程确实是鸡肋， 效果不如多进程。
    这是因为多线程完成计算密集型任务时，任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低。
    对于IO密集型任务，多线程能够有效提升效率。 
    这是因为单线程下有IO操作时，会进行IO等待，造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率。
    需要注意的时，对于IO密集型任务，在Python中也有较好的解决方式——协程，在后续文章会详细讨论。

# python协程

    参考网址：https://blog.csdn.net/Cyrus_May/article/details/122491335
    方案：
    greenlet模块（早期）
    yield关键字
    asyncio模块（py3.4）
    async、await关键字（py3.5）

    作用:
    在一个线程中，如果遇到IO等待时间，利用该空闲时间去处理其余任务。

# sqlite

    Sqlite没有实现TRUNCATE表操作，可以使用如下两条语句来清空表并重置起始索引号：
    delete from 表名;
    DELETE FROM sqlite_sequence WHERE name = '表名';

# 代码片段

    ${PROJECT_NAME} 项目名称
    ${PRODUCT_NAME} IDE的名称
    ${NAME} 文件名称
    ${USER} 用户的登录名
    ${DATE} 日期
    ${TIME} 时间
    ${YEAR} 年
    ${MONTH} 月
    ${DAY} 日
    ${HOUR} 时
    ${MINUTE} 分

# sqlalchemy

    # alter table user alter column ids set default '' 修改数据库列默认值
    数据库生成model: sqlacodegen 'mysql+pymysql://root:xl123456?@47.105.50.31:3306/myboot' --outfile=models.py
    1.first, 一条结果，没有返回None,不抛出异常
    2.all，返回一个list
    3.one，没有数据或者有多个都会抛出异常
    4.one_or_none
    5.scalar,一条，若有多条结果抛出异常