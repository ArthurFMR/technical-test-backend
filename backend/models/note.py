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
    def find_all(cls, _id: int) -> List["Note"]:
        return cls.select().where(cls.user == _id)
    
    @classmethod
    def find_by_title(cls, title: str) -> "Note":
        return cls.get(cls.title == title)
