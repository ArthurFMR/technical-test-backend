from enum import unique
from ..pw_db import BaseModel
import peewee as pw


class User(BaseModel):
    username = pw.CharField(unique=True)
    password = pw.CharField()

    @classmethod
    def find_by_username(cls, username: str) -> "User":
        return cls.get(cls.username == username)
