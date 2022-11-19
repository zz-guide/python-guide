import sqlite3

conn = sqlite3.connect('t_sqlite.db')


def func_main():
    # create_db()
    # insert_db()
    # query_db()
    # update_db()
    # delete_db()
    pass


def create_db():
    print("数据库打开成功")
    c = conn.cursor()
    sql = """CREATE TABLE student
           (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name           TEXT    NOT NULL,
               age            INT     NOT NULL,
               address        CHAR(50)
           );"""
    c.execute(sql)
    print("数据表创建成功")
    conn.commit()
    conn.close()
    pass


def insert_db():
    c = conn.cursor()
    c.execute("INSERT INTO student (name,age,address) VALUES ( '许磊', 32, '地址1' )")
    c.execute("INSERT INTO student (name,age,address) VALUES ( '张三', 22, '地址2' )")

    conn.commit()
    print("数据插入成功")
    conn.close()


def query_db():
    c = conn.cursor()
    cursor = c.execute("SELECT id, name, age, address  from student")
    for row in cursor:
        print("id = ", row[0])
        print("name = ", row[1])
        print("age = ", row[2])
        print("address = ", row[3], "\n")

    print("数据操作成功")
    conn.close()
    pass


def update_db():
    c = conn.cursor()
    c.execute("UPDATE student set address = 'aksjhdk' where id=1")
    conn.commit()
    print("Total number of rows updated :", conn.total_changes)
    cursor = conn.execute("SELECT id, name, age, address  from student")
    for row in cursor:
        print("id = ", row[0])
        print("name = ", row[1])
        print("age = ", row[2])
        print("address = ", row[3], "\n")

    print("数据操作成功")
    conn.close()
    pass


def delete_db():
    c = conn.cursor()
    print("数据库打开成功")
    c.execute("DELETE from student where id=1;")
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)

    cursor = conn.execute("SELECT id, name, address,age  from student")
    for row in cursor:
        print("id = ", row[0])
        print("name = ", row[1])
        print("age = ", row[2])
        print("address = ", row[3], "\n")

    print("数据操作成功")
    conn.close()
    pass
