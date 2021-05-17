from bottle import Bottle, response
from resources import user

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


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
