def arg_func(n):
    """
    1. name 后边什么都不写，代表是必传参数，不传就抛TypeError异常。
    2. 虽然传了，但是避免不了值为None
    3. 可以传递与指定类型不一致的值，不是强制的

    """
    print("n:", n)


if __name__ == "__main__":
    name = ""
    arg_func(name)
