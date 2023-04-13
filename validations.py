import re
from functools import wraps
from flask import jsonify, request
import jwt
from config import *

def valPassword(passwd):
    if len(passwd) < 8:
        return False
    if len(passwd) > 50:
        return False
    if not re.search("[a-z]", passwd):
        return False
    if not re.search("[A-Z]", passwd):
        return False
    if not re.search("[0-9]", passwd):
        return False
    return True

def valNames(name):
    if not re.fullmatch("[A-Za-z]{2,25}||\s[A-Za-z]{2,25}", name):
        return False
    return True

def valEmail(email):
    if not re.search("^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
        return False
    return True

def valStatus(status):
    if not re.fullmatch("[pP]|[dD]?", status):
        return False
    return True

def valModel(model):
    if not re.fullmatch("[A-Za-z0-9]{1,30}", model):
        return False
    return True

def valPlate(plate):
    if not re.fullmatch("[A-Z0-9]{1,9}", plate):
        return False
    return True

def valKilometers(kilometers):
    if not re.fullmatch("[0-9]{2,1000000}", kilometers):
        return False
    return True

def tokenRequired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.json['token']
        if not token:
            return jsonify({'message': 'token is missing!'}), 403
        try:
            access_token = jwt.decode(token, secretKeyToken, verify=True, algorithms=["HS256"])
        except:
            return jsonify({'message': 'token is invalid'}), 403
        return f(*args, *kwargs)
    return decorated
