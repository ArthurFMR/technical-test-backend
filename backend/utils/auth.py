from bottle import request, response


# Decorator for protect routes
def token_required(func):
    def wrapper():
        if request.method != 'OPTIONS':  # Avoiding Preflight request
            token = request.headers.get('authorization')
            if not token or token == 'null':
                response.status = 403
                return {"error": "Access denied. Token is Missing"}
            return func(token)
    return wrapper
