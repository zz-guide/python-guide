def func_main():
    func_with()
    pass


def func_no_try():
    # 以下代码如果在调用 write 的过程中，出现了异常，则 close 方法将无法被执行，
    # 因此资源就会一直被该程序占用而无法被释放。
    # 我们可以使用 try…except…finally 来改进代码
    file = open('./ttt.txt', 'w')
    file.write('hello world !')
    file.close()


def func_try():
    file = open('./ttt.txt', 'w')
    try:
        file.write('hello world')
    finally:
        file.close()


def func_with():
    # 使用 with 关键字系统会自动调用 f.close() 方法， with 的作用等效于 try/finally 语句是一样的。
    # with 语句实现原理建立在上下文管理器之上。
    # 上下文管理器是一个实现 __enter__ 和 __exit__ 方法的类。
    # 使用 with 语句确保在嵌套块的末尾调用 __exit__ 方法。
    # 在文件对象中定义了 __enter__ 和 __exit__ 方法，
    # 即文件对象也实现了上下文管理器，首先调用 __enter__ 方法，
    # 然后执行 with 语句中的代码，最后调用 __exit__ 方法。 即使出现错误，
    # 也会调用 __exit__ 方法，也就是会关闭文件流。
    with open('./ttt.txt', 'w') as file:
        file.write('hello world !')
