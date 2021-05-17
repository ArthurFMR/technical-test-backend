import peewee

db = peewee.SqliteDatabase('notes.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db
