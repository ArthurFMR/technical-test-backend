from bottle import Bottle, response

from resources import user, note
from utils.auth import token_required


app = Bottle()


@app.hook('after_request')
def set_headers():
    response.content_type = 'application/json'


@app.post('/users/register')
def register_user():
    return user.register_user()


@app.post('/users/login')
def login_user():
    return user.login_user()


@app.post('/notes')
@token_required
def create_note(token):
    return note.create_note(token)


@app.get('/notes')
@token_required
def get_notes(token):
    return note.get_notes(token)


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
