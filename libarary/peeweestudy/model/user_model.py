from datetime import datetime
from peewee import *
from .base_model import BaseModel


class UserModel(BaseModel):
    name = TextField()
    username = TextField(unique=True)
    password = TextField(default='')
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "user"
