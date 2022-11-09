def func_main():
    num = 14

    # 进入else会退出while循环，不需要使用break
    while num > 12:
        print("大于")
        num = num - 1
    else:
        print("小于")
