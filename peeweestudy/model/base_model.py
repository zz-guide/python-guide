from peewee import SqliteDatabase, Model

import logging

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
db = SqliteDatabase('/Users/xulei/Downloads/user.db')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db
