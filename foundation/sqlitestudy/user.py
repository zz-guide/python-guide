# from src.backend.util.db_cache import DbCache
# from src.backend.util.sql import SqlUtil
# 初始化数据库实例
# def __load_db():
#     DbCache.conn = sqlite3.connect(PathUtil.get_db_path('user'))
#     DbCache.cursor = DbCache.conn.cursor()

CREATE_SQL = """
CREATE TABLE user
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT     NOT NULL,
       username       TEXT UNIQUE NOT NULL,
       password       CHAR(20)  NOT NULL,
       created_at     TEXT NOT NULL,
       updated_at     TEXT NOT NULL)
"""


class UserModel:
    table_name = 'user'

    def __init__(self):
        pass


class UserService:
    @staticmethod
    def create_table() -> bool:
        res = DbCache.cursor.execute(SqlUtil.get_table_exists_sql(UserModel.table_name)).fetchone()
        if res:
            return True
        DbCache.cursor.execute(CREATE_SQL)
        DbCache.conn.commit()
        return True

    @staticmethod
    def getById() -> [UserModel, None]:
        res = DbCache.cursor.execute(f'SELECT *  from {UserModel.table_name}').fetchone()
        if res:
            return UserModel()

        return None
