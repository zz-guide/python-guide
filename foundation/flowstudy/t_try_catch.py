def func_main():
    # raise Exception("没有处理异常")

    # 不处理异常程序就会停止运行
    try:
        print("try 可能发生异常的代码块")
        num = 20
        if num > 12:
            print("大于")
        else:
            print("小于")
        raise Exception("主动出错了")
    except Exception as err:
        print("except异常", err)
    else:
        print("else 没有发生异常时执行代码")
    finally:
        print("finally 不管有没有异常都会执行")
