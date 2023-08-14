# 使用PySide6开发GUI，

# 网址：https://doc.qt.io/qtforpython-6/

# 网址：https://pypi.org/project/PyQt6/

# pycharm参考设置： https://blog.csdn.net/ly1358152944/article/details/127323598

# QT for Python 官方文档：https://doc.qt.io/qtforpython/

# SizePolicy

    Fixed：控件不能放大或者缩小，控件的大小就是它的sizeHint。
    Minimum：控件的sizeHint为控件的最小尺寸。控件不能小于这个sizeHint，但是可以放大。
    Maximum：控件的sizeHint为控件的最大尺寸，控件不能放大，但是可以缩小到它的最小的允许尺寸。
    Preferred：控件的sizeHint是它的sizeHint，但是可以放大或者缩小。
    Expanding：控件可以自行增大或者缩小。
    sizeHint（布局管理中的控件默认尺寸，如果控件不在布局管理中就为无效的值）

    sizeHint：为布局管理器中部件的缺省大小，如果部件不在布局管理中就为无效的值，该值是Qt中对每个部件大小的建议值，也是缺省值，不能修改；
    minimumSizeHint：为Qt推荐的部件最小大小，如果部件不在布局管理中就为无效的值，在布局管理器中minimumSizeHint 就是部件的缺省最小值，除非当前部件的大小策略为QSizePolicy.Ignore或者minimumSize被设置，布局管理器不会调整一个部件的大小到比minimumSizeHint 返回值更小的大小；
    minimumSize：minimumSize为部件的最小大小，部件尺寸缩放时不允许比minimumSize更小，如果部件大小被设置为QSize(0, 0)，则minimumSize将失效。一般控件的这个值缺省为QSize(0, 0)。该值可以调用setMinimumSize进行调整。

# 槽和函数

    参考网址：https://blog.csdn.net/freeking101/article/details/125053831
    网址：https://maicss.gitbook.io/pyqt-chinese-tutoral/pyqt6/dialogs

# 问题

    1.os._exit()和sys.exit()区别
    2.sys.argv()
    3.super()
    4.MRO 方法解析顺序(Method Resolution Order)
    5.spec文件如何生成
    6.requirement.txt文件如何生成
    7.打包二进制：pyinstaller -i icon.ico -F temp.py
      pyinstaller -F XXXX.spec
    8.槽函数可以定义在其他类，但是绑定操作得定义在组件
    9.自定义信号触发，槽函数返回值怎么办？
    10.槽函数装饰器有什么用？
    11.自动链接信号目前测试的结果是动态加载ui不能，静态的可以。

# peewee

    1.根据数据库生成模型
        python -m pwiz -e postgresql charles_blog > blog_models.py

    Comparison	Meaning
    ==	x equals y
    <	x is less than y
    <=	x is less than or equal to y
    >	x is greater than y
    >=	x is greater than or equal to y
    !=	x is not equal to y
    <<	x IN y, where y is a list or query
    >>	x IS y, where y is None/NULL
    %	x LIKE y where y may contain wildcards
    **	x ILIKE y where y may contain wildcards
    ^	x XOR y
    ~	Unary negation (e.g., NOT x)

# 重置自增id

    1.delete from 表名
    2.update sqlite_sequence set seq = 0 where name = '表名'
    3.或者 delete from sqlite_sequence where name = '表名'

# sqlite

    1.唯一约束与唯一索引的区别
    网址：https://blog.csdn.net/llzd626/article/details/120073597
    2.model目前不能针对所有数据库进行统一定义，需要做一些小适配

# 问题

    1.pyside代码中非常容易出现循环import的场景，即A->B,B->A,导致初始化的变量有依赖
    2.自定义信号的问题，必须定义成成员变量，然后也容易在各个widget之间耦合
    3.QTSQL，QTHREAD，QMUTEX