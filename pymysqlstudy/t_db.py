import pymysql

# 参考：https://blog.csdn.net/u013066730/article/details/116596370
# 参考：https://github.com/PyMySQL/PyMySQL/blob/main/example.py
conn = pymysql.connect(
    host="47.105.50.31",
    port=3306,
    user='root',  # 在这里输入用户名
    password='xl123456?',  # 在这里输入密码
    charset='utf8mb4',
    database='myboot',
)  # 连接数据库

cursor = conn.cursor()


def func_main():
    func_query()
    pass


def func_query():
    sql = "select * from user"
    # 执行SQL语句
    res = cursor.execute(sql)
    print(res)

    # 光标按绝对位置移动1
    # cursor.scroll(1, mode="absolute")
    # 光标按照相对位置(当前位置)移动1
    # cursor.scroll(1, mode="relative")

    # 取到查询结果
    ret1 = cursor.fetchone()  # 取一条
    print(ret1)
    ret2 = cursor.fetchmany(3)  # 取三条
    print(ret2)
    ret3 = cursor.fetchone()  # 取一条
    print(ret3, type(ret3))  # 结果是一个元组

    func_close()
    pass


def func_close():
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
    pass
