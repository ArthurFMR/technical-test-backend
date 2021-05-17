from bottle import request
from bottle import HTTPResponse as http_res

from marshmallow import ValidationError

from models.user import User
from schemas.user import UserSchema

from utils.manage_token import create_token


user_schema = UserSchema()


def register_user():
    user_json = request.json

    # Validation of data
    try:
        user_data = user_schema.load(user_json).data
    except ValidationError as err:
        body = {"errors": err.messages}
        return http_res(status=422, body=body)

    # Checking if username already exists
    try:
        User.find_by_username(user_data['username'])
        message = "That username already exists"
        return http_res(status=400, body={"errors": message})
    except:
        user = User.create(**user_data)
        body = {"user": user_schema.dump(user).data}
        return http_res(status=201, body=body)


def login_user():
    user_json = request.json

    # Validation of data
    try:
        user_data = user_schema.load(user_json).data
    except ValidationError as err:
        body = {"errors": err.messages}
        return http_res(status=422, body=body)

    # Authentication and create token
    try:
        user = User.find_by_username(user_data['username'])
        if user.password == user_data["password"]:
            token = create_token({'identity': user.id})
            body = {"token": token}
            return http_res(status=200, body=body)
        raise ValueError
    except:
        body = {"errors": "Invalid credentials"}
        return http_res(status=400, body=body)
