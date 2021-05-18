from bottle import request, response
from bottle import HTTPResponse as http_res

from marshmallow import ValidationError

from models.user import User
from schemas.user import UserSchema

from utils.manage_token import create_token

import json

user_schema = UserSchema()


def register_user():

    user_json = request.json

    # Validation of data
    try:
        user_data = user_schema.load(user_json).data
    except ValidationError as err:
        response.status = 422
        return {"errors": err.messages}

    # Checking if username already exists
    try:
        User.find_by_username(user_data['username'])
        response.status = 400
        return json.dumps({"error": "That username already exists"})
    except:
        user = User.create(**user_data)
        body = {"user": user_schema.dump(user).data}
        return body


def login_user():
    user_json = request.json

    # Validation of data
    try:
        user_data = user_schema.load(user_json).data
    except ValidationError as err:
        response.status = 422
        return {"errors": err.messages}

    # Authentication and create token
    try:
        user = User.find_by_username(user_data['username'])
        if user.password == user_data["password"]:
            token = create_token({'identity': user.id})
            return {"token": token}
        raise ValueError
    except:
        response.status = 400
        return {"errors": "Invalid credentials"}
