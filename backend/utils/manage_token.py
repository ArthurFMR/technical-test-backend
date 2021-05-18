import jwt

secret_key = "b'855119b3c4e5e95d7f9ff51e06277963'"


def create_token(data):
    token = jwt.encode(data, secret_key, algorithm='HS256').decode('utf-8')
    return token


def decode_token(token):
    if "Bearer" in token:  # if the token come with Bearer header, remove it
        token = token.replace('Bearer ', '')
    data = jwt.decode(token, secret_key, algorithms=['HS256'])
    return data
