import logging

# 针对 basicConfig 进行配置(basicConfig 其实就是对 logging 模块进行动态的调整，之后可以直接使用)
# format具体格式如下：
# 格式符	含义
# %(levername)s	日志级别名称
# %(pathname)s	当前执行程序的路径(即脚本所在的位置)
# %(filename)s	执行脚本程序名
# %(lineno)d	日志当前的行号
# %(asctime)s	打印日志的时间
# %(message)s	日志信息
# 常用的日志 fromat 常用方案：fromat = '%(asctime)s %(filename)s[line:%(lineno)d] %(levername)s %(message)s'

# logging.basicConfig(
#     level=logging.INFO,  # INFO 等级以下的日志不会被记录
#     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # 日志输出格式
#     filename='run.log',  # 日志存放路径(存放在当前相对路径)
#     filemode='a',  # 输入模式；如果当前我们文件已经存在，可以使用 'a' 模式替代 'w' 模式
# )
#
#
# def func_main():
#     logging.debug('这是一条 debug 信息')
#     logging.info('这是一条 日志记录 信息')
#     logging.warning('这是一条 警告 信息')
#     logging.error('这是一条 重大的错误 信息')
