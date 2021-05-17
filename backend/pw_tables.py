from models import user, notes
from models.base_model import db

db.create_tables([user.User, notes.Note])

