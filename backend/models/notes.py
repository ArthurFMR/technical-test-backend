from .base_model import BaseModel
import peewee as pw
from datetime import datetime
from .user import User
from typing import List


class Note(BaseModel):
    title = pw.CharField(unique=True)
    description = pw.TextField()
    created_date = pw.DateTimeField(default=datetime.now)
    user = pw.ForeignKeyField(User, related_name="notes")

    @classmethod
    def find_all(cls, _id: int) -> List["Notes"]:
        return cls.select().where(User.id == _id)
