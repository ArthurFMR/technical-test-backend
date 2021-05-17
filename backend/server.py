from bottle import Bottle

app = Bottle()


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
