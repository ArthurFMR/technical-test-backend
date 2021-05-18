from bottle import Bottle, response, request

from resources import user, note
from utils.auth import token_required


app = Bottle()


@app.hook('after_request')
def set_headers():
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5000'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, Authorization'
    response.content_type = 'application/json'


@app.route('/users/register', method=['POST', 'OPTIONS'])
def register_user():
    if request.method == 'POST':
        return user.register_user()


@app.route('/users/login', method=['POST', 'OPTIONS'])
def login_user():
    if request.method == 'POST':
        return user.login_user()


@app.route('/notes', method=['POST', 'OPTIONS'])
@token_required
def create_note(token):
    return note.create_note(token)


@app.get('/notes')
@token_required
def get_notes(token):
    return note.get_notes(token)


if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)
