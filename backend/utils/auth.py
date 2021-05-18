from bottle import request, response


def token_required(func):
    def wrapper():
        token = request.headers.get('authorization')
        if not token:
            response.status = 403
            return {"error": "Access denied. Token is Missing"}
        return func(token)
    return wrapper
