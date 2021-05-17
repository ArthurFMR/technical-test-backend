from models import user, note
from models.base_model import db

db.create_tables([user.User, note.Note])
