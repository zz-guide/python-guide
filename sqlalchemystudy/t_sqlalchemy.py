from sqlalchemystudy.t_db import DbManager

from sqlalchemystudy.t_model import User

manager = DbManager()
session = manager.get_session()


def func_main():
    func_curd()
    pass


def func_curd():
    # insert_user()
    # query_user()
    # update_user()
    delete_user()
    pass


# 创建新的User对象
def insert_user():
    names = {'Jeny': 22}
    for key, value in names.items():
        print(key, value, type(key), type(value))
        user = User(name=key, age=value)
        print(user)
        session.add(user)
    session.commit()
    manager.close_session()


def query_user():
    users = session.query(User).all()
    for item in users:
        print(item)

    user = session.query(User).filter(User.id == 1).one()
    print(user)
    # manager.close_session()


def update_user():
    user = session.query(User).filter(User.id == 1).update({User.name: "ben"})
    print(user)
    # session.commit()
    # manager.close_session()


def delete_user():
    user = session.query(User).filter(User.id == 6).delete()
    print(user)
    # session.commit()
    # manager.close_session()
