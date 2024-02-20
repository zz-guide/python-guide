import time


def func_main():
    func_time()
    pass


def func_time():
    # 获取当前时间戳
    # timestamp = time.time()
    # timestamp = time.localtime()
    # print('当前时间戳:', timestamp)

    # 当前日期时间
    date_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print('当前日期时间：', date_time_str)
    # 当前日期时间，带中文
    date_time_str = time.strftime('%Y{}%m{}%d{} %H{}%M{}%S{}', time.localtime()).format("年", "月", "日", "时", "分",
                                                                                        "秒")
    print('当前日期时间(中文)：', date_time_str)


if __name__ == '__main__':
    func_main()
