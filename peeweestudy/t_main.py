from datetime import date

from peewee import chunked

from .model import UserModel
from playhouse.shortcuts import dict_to_model, model_to_dict


def func_main():
    # insert()
    # batch_insert()
    query()
    pass


def insert():
    data = {'username': 'xulei2', 'password': '12344'}
    # create(),创建成功返回一个实例
    user = UserModel.create(**data)

    # save()默认是插入，如果提供了主键，则变为update语句
    # 指定id创建，save（）需要指定force_insert=True,否则id存在就会修改数据，可通过sql观察
    user = UserModel(**data)
    res = user.save(force_insert=True)

    # insert,只插入数据而不创建模型实例，返回新行的主键。
    res = UserModel.insert(**data).execute()

    print("res=", res, ",type=", type(res))
    print(user.id, user.password, user.username)


def batch_insert():
    # insert_many 元组列表
    # data = [
    #     ('张三', 'zhangsan', '123456'),
    #     ('李四', 'lisi', '123456'),
    #     ('王五', 'wangwu', '123456'),
    #     ('赵六', 'zhaoliu', '123456'),
    # ]
    # columns = ['name', 'username', 'password']
    # with UserModel._meta.database.atomic():
    #     res = UserModel.insert_many(data, columns).execute()
    #     print('res:', res)

    # 字典列表
    # data1 = [
    #     {'name': '张三', 'username': 'zhangsan', 'password': '123456'},
    #     {'name': '李四', 'username': 'lisi', 'password': '123456'},
    #     {'name': '王五', 'username': 'wangwu', 'password': '123456'},
    #     {'name': '赵六', 'username': 'zhaoliu', 'password': '123456'}
    # ]
    # with UserModel._meta.database.atomic():
    #      # 返回的是最后一条插入数据的id
    #     res = UserModel.insert_many(data1).execute()
    #     print('res:', res)

    # sqlite批量插入有限制，999
    # with UserModel._meta.database.atomic():
    #     for idx in range(0, len(data1), 100):
    #         UserModel.insert_many(data1[idx: idx + 100]).execute()
    # 或者
    # with UserModel._meta.database.atomic():
    #     for batch in chunked(data, 100):
    #         UserModel.insert_many(batch).execute()

    # bulk_create(model_list, batch_size=None)
    # 简单来说，insert_many 使用字典或元组列表作为参数，而 model_list 使用模型实例列表作为参数，就这区别。

    # insert_from
    # 使用 SELECT 查询作为源 INSERT 数据。此 API 应用于 INSERT INTO ... SELECT FROM ... 形式的查询。
    # 因为是 INSERT INTO ... SELECT FROM ... 形式的，所以数据源的列跟要插入的列必须保持一致。
    # data = UserModel.select(UserModel.name, UserModel.username, UserModel.password)
    # UserModel2.insert_from(data, ['name', 'username', 'password']).execute()
    pass


def query():
    # 根据name查询,get_or_none 不抛出异常，get()会抛出异常
    # user = UserModel.select().where(UserModel.name == 'xulei').get_or_none()
    # 根据id查询,但是不知道怎么筛选字段
    # user = UserModel.get_by_id(9)
    # 复杂查询

    # select() 返回结果是一个 ModelSelect 对象，该对象可迭代、索引、切片。当查询不到结果时，不报错，返回 None。并且 select() 结果是延时返回的。如果想立即执行，可以调用 execute() 方法。
    user = UserModel.select(UserModel.name).order_by(
        UserModel.created_at.desc())
    print(user)
    # print(user.username, user.password)


def update():
    pass


def delete():
    # 根据条件删除
    UserModel.delete().where(UserModel.Name == '王五').execute()
    # 如果是查询出来的实例，可以直接删除
    user = UserModel.get(UserModel.Name == 'xulei')
    user.delete_instance()
    pass
