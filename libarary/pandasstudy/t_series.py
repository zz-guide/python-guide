import pandas as pd


def func_main():
    creat_series()
    pass


def creat_series():
    # series就是一个一维数据，里边可以是各种数据类型，索引可以自定义
    # 整体感觉就是一个map
    # series = pd.Series([123, '456', 789], index=[1, 2, 3])
    # print(type(series))  # <class 'pandas.core.series.Series'>
    # print(series)

    # 若数据类型不一致，就是object
    # 传入一个dict会自动构建索引
    # 若传入dict,重新指定index会报错
    # 若index数量不一致，不会报错
    # series = pd.Series({'name': '许磊', 'age': '22', 'address': '地址'}, index=['a', 'b', 'c', 'd'])
    series = pd.Series({'name': '许磊', 'age': '22', 'address': '地址'})
    print(series)

    print(series.index)
    print(series.values)
    pass
