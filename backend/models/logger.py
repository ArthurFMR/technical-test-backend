from enum import unique
from ..pw_db import BaseModel
import peewee as pw


class Logger(BaseModel):
    token = pw.CharField(unique=True)

    @classmethod
    def find(cls, token: str) -> "Logger":
        return cls.get(cls.token == token)