import peewee

db = peewee.SqliteDatabase('notes.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([])