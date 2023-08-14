import numpy as np
import pandas as pd


def func_main():
    creat_dataframe()
    pass


def creat_dataframe():
    res = pd.read_csv('./pandasstudy/student.csv')
    # print(res.head())
    # print(res.tail())
    # print(res.columns)
    # print(res.index)
    # print(res.shape)
    # print(res.values)
    # print(res.T)  # 转置就是互换行和列
    # print(res)
    # print('---------')
    # res = res.reset_index()
    # print(res)
    # print(res.columns)
    # print(res.index)

    # loc方法是通过行、列的名称或者标签来寻找我们需要的值。
    # loc属性访问数据，第一个参数是index,第二个参数是column,:表示所有，[]里边为先行后列。
    # print(res.loc[0, 'Id'], res.loc[0, 'Name'], res.loc[0, 'Age'])
    # 读取第二行的值,得到一个series
    # rr = res.loc[1]
    # print(rr)
    # 读取第二列的值
    # print(res.loc[:, 'Name'])
    # 读取某个区域内的数据,注意与python原生的截取不同，包含左右两边的数据
    # print(res.loc[0:1, 'Id':'Name'])
    # 根据条件读取,两者等价
    # print(res.loc[res.Id > 2, ['Id', 'Name']])
    # print(res[res.Id > 2])
    # iloc方法是通过索引行、列的索引位置[index, columns]来寻找值

    # 读取第二行d的值
    # print(res.iloc[1])
    # print('----------')
    # print(res.iloc[1, :])  # 效果与上面相同
    # 读取第二列的值,iloc不需要知道名字，而是通过指定位置来访问
    # print(res.iloc[:, 1])
    # 同时读取某行某列
    print(res.iloc[1, 1])
    # 读取第2、3行，第3、4列
    # print(res.iloc[1:3, 2:4])
    # 参考：https://blog.csdn.net/weixin_45969777/article/details/125331109
    # 条件，合并，排序，分组，平均
    pass
