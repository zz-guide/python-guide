# 机器学习

# pandas学习

# Series

    Series是一个类似于一维数组的数据结构，它能够保存任何类型的数据，比如整数、字符串、浮点数等，
    主要由一组数据和与之相关的索引两部分构成。

    ①Series的创建
    pd.Series(data=None, index=None, dtype=None)
    data：传入的数据，可以是字典、list等
    index：索引，必须是唯一的，且与数据的长度相等。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
    dtype：数据的类型

    ②series的属性
    为了更方便地操作Series对象中的索引和数据，Series中提供了两个属性index和values

# DataFrame

    DataFrame是一个类似于 二维数组或表格(如excel) 的对象，既有行索引，又有列索引
    行索引，表明不同行，叫index，0轴，axis=0
    列索引，表明不同列，叫columns，1轴，axis=1
    ① DataFrame的创建
    pd.DataFrame(data=None, index=None, columns=None)
    index：行标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
    columns：列标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。

    ② DataFrame的属性
    shape
    获得DataFrame的形状（行数、列数）

    index
    获得DataFrame的行标签（索引）

    columns
    获得DataFrame的列标签

    values
    获得DataFrame的所有值

    T
    将DataFrame的转置
    数组转置是将矩阵的行列互换得到的新矩阵称为转置矩阵，转置矩阵的行列式不变。
    由定义可知，A为M乘N矩阵，则 A的转置为N乘M矩阵。
    运算法则：
    A的转置的转置等于A。A加B转置等于A的转置加B的转置。K倍A的转置等于K乘A的转置。A乘B的转置等于B的转置乘A的转置。

    head()
    输出DataFrame的前几条数据，默认为5

    tail()
    输出DataFrame的后几条数据，默认为5

    ③DatatFrame索引的修改
    datatframe.reset_index(drop=False)
    设置新的下标索引，drop默认为False，意为不删除原来索引；如果为True，则删除原来的索引

    ④重新设置索引
    datatframe.set_index(keys, drop=True)
    以现有的某列值将其设置为新的索引
    keys：列索引名或者列表
    drop：布尔类型，默认为真，删除原来的索引

# df的loc与iloc用法详解

    loc为Selection by Label函数，即为按标签取数据
    loc属性访问数据，第一个参数是index,第二个参数是column,:表示所有，[]里边为先行后列。
    loc函数：第一个参数取行，第二个参数取列。取行用行索引值，取列用列名，都是前闭后闭
    iloc函数：第一个参数取行，第二个参数取列。取行用行索号，取列用列名的下标，都是前闭后开
    注：loc是location的意思，iloc中的i是integer的意思，仅接受整数作为参数。

# MultiIndex(老版本中叫Panel) 