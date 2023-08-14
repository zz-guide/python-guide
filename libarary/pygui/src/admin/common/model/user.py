from peewee import CharField, DateTimeField, SQL

from ._base import BaseModel
from src.common.util import now


class User(BaseModel):
    name = CharField(constraints=[SQL("DEFAULT ''")], default='')
    username = CharField(constraints=[SQL("DEFAULT ''"), SQL('UNIQUE')], unique=True)
    password = CharField(constraints=[SQL("DEFAULT ''")], default='')
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], default=now)
    updated_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], default=now)
    data_updated_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')], default=now)

    class Meta:
        table_name = 'user'
