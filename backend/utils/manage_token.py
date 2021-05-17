import jwt

secret = "b'855119b3c4e5e95d7f9ff51e06277963'"


def create_token(data):
    token = jwt.encode(data, secret, algorithm='HS256').decode('utf-8')
    return token


def decode_token(bearer_token):
    token = bearer_token.replace('Bearer ', '')
    data = jwt.decode(token, secret, algorithms=['HS256'])
    return data
