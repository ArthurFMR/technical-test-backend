from bottle import request, abort
from bottle import HTTPResponse as http_res


def token_required(func):
    def wrapper():
        token = request.headers.get('authorization')
        if not token:
            body = {"errors": "Access denied. Token is Missing"}
            return http_res(status=403, body=body)
        return func(token)
    return wrapper