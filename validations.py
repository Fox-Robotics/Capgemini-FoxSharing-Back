import re
from functools import wraps
from flask import jsonify, request
import jwt
from databaseConection import *

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

def valRole(role):
    if not re.fullmatch("[aA]|[bB]?", role):
        return False
    return True

def valModelo(modelo):
    if not re.fullmatch("[A-Za-z0-9]{1,30}", modelo):
        return False
    return True

def valPlacas(placas):
    if not re.fullmatch("[A-Z0-9]{1,9}", placas):
        return False
    return True

def valKilometros(kilometros):
    if not re.fullmatch("[0-9]{2,1000000}", kilometros):
        return False
    return True

def tokenRequired(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.json['token']
        if not token:
            return jsonify({'message': 'token is missing!'}), 403
        try:
            access_token = jwt.decode(token, secretKey, verify=True, algorithms=["HS256"])
        except:
            return jsonify({'message': 'token is invalid'}), 403
        return f(*args, *kwargs)
    return decorated

def validate_credit_card(card_number: str) -> bool:
    card_number = [int(num) for num in card_number]
    checkDigit = card_number.pop(-1)
    card_number.reverse()
    card_number = [num * 2 if idx % 2 == 0
                   else num for idx, num in enumerate(card_number)]
    card_number = [num - 9 if idx % 2 == 0 and num > 9
                   else num for idx, num in enumerate(card_number)]
    card_number.append(checkDigit)
    checkSum = sum(card_number)
    return checkSum % 10 == 0
