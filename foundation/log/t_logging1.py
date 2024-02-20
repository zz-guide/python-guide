import logging
import os


def init_log(path):
    if os.path.exists(path):
        mode = 'a'
    else:
        mode = 'w'
    logging.basicConfig(  # 针对 basicConfig 进行配置(basicConfig 其实就是对 logging 模块进行动态的调整，之后可以直接使用)
        level=logging.INFO,  # INFO 等级以下的日志不会被记录
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # 日志输出格式
        filename='run1.log',  # 日志存放路径(存放在当前相对路径)
        filemode=mode,  # 输入模式；如果当前我们文件已经存在，可以使用 'a' 模式替代 'w' 模式
        # 与文件写入的模式相似，'w' 模式为没有文件时创建文件；'a' 模式为追加内容写入日志文件
    )

    # return logging


def func_main():
    current_path = os.getcwd()
    print(current_path)
    path = os.path.join(current_path, 'run1.log')
    print(path)
    init_log(path)  # 初始化返回的 init_log() 函数 , 其实就是 return logging
    # print(type(log))
    logging.debug('这是一条 debug 信息 ---> 第三次写入')
    logging.info('这是一条 日志记录 信息 ---> 第三次写入')
    logging.warning('这是一条 警告 信息 ---> 第三次写入')
    logging.error('这是一条 重大的错误 信息 ---> 第三次写入')
