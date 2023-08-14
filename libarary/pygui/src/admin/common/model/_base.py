import os
import logging

from peewee import SqliteDatabase, Model
from playhouse.shortcuts import model_to_dict
from src.common import VariableCache

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

# todo::暂时没有想到好方法区初始化这个变量
path = os.getcwd()
VariableCache.database = SqliteDatabase(f'{path}/gui.db', autoconnect=False)
VariableCache.database.connect(reuse_if_open=True)


class BaseModel(Model):
    class Meta:
        database = VariableCache.database

    def model_to_dict(self):
        return model_to_dict(self)
