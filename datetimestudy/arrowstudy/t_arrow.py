import time

import arrow

"""
参考网址：https://arrow.readthedocs.io/en/latest/guide.html#format
"""


def func_main():
    # print('asdasd')
    # func_t()
    func_t1()
    pass


def func_t():
    # 获取世界标准时间
    # utc_time = arrow.utcnow()
    # print(utc_time)

    # 获取指定时区的时间
    # US_time = arrow.now('US/Pacific')
    # print(US_time)

    # 获取本地时间
    # local_time = arrow.now()
    # print(local_time)

    float_timestamp = time.time()
    print(float_timestamp)
    time_tmp = arrow.get(float_timestamp)
    print(time_tmp)


def func_t1():
    # 将字符串转换为arrow对象
    # aa = arrow.get("2022-08-17 20:00:00", "YYYY-MM-DD HH:mm:ss")
    # print(aa)

    # 当前时间戳->字符串
    # res = arrow.now().format() # 2022-11-28 16:33:51+08:00
    res = arrow.now().format('YYYY-MM-DD HH:mm:ss ZZ')  # 2022-11-28 16:34:04 +08:00
    print(res)


if __name__ == '__main__':
    func_main()
