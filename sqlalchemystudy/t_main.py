from sqlalchemystudy.db import session
from sqlalchemystudy.service.user import UserService


def func_main():
    # t_insert()
    t_query()
    # t_delete()
    pass


def t_insert():
    UserService.insert()


def t_delete():
    # 1.根据传入的值直接删除
    # res = UserService.delete_by_id(22)
    # 2.根据已存在的model对象删除
    user = UserService.get_by_id(1)
    session.delete(user)
    session.commit()
    session.close()


def t_update():
    pass


def t_query():
    # 测试查询
    # user = UserService.get_by_id(12)
    # if not user:
    #     print('记录不存在')
    # else:
    #     print(user)

    # 查询全部数据+排序
    # users = UserService.get_all()
    # if not users:
    #     print('记录不存在')
    # else:
    #     for user in users:
    #         print(user.id, user)

    # in 查询
    # users = UserService.get_by_ids([6, 7, 8])
    # if not users:
    #     print('记录不存在')
    # else:
    #     for user in users:
    #         print(user.id, user)

    # like查询
    # users = UserService.get_name_like('许磊')
    # if not users:
    #     print('记录不存在')
    # else:
    #     for user in users:
    #         print(user.id, user)
    # count
    # count = UserService.get_count()
    # print('总记录数:', count)

    # 动态where
    # users = UserService.page_search()
    # if not users:
    #     print('记录不存在')
    # else:
    #     for user in users:
    #         print(user.id, user)

    # 聚合函数，sum,count,max,min,having,group_by
    user = UserService.get_count_id()
    print(user)


if __name__ == '__main__':
    func_main()
