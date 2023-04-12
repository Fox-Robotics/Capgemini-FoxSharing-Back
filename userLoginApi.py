import datetime
from flask import jsonify, request, Blueprint
import bcrypt, jwt
from databaseConection import mycursor, db
from config import secretKeyToken

userLoginBP = Blueprint('userLoginBP', __name__)

@userLoginBP.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password'].encode('UTF-8')
    mycursor.execute("SELECT hash FROM Users WHERE email = %(email)s", {"email": email})
    values = mycursor.fetchone()
    if values is None:
        return jsonify({"message": "Incorrect Email"})
    else:
        pswd = values[0].encode('UTF-8')
        if bcrypt.hashpw(password,pswd) == pswd:
            payload = {
                "sub": email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }
            token = jwt.encode(payload, secretKeyToken, algorithm='HS256')
            mycursor.reset()
            mycursor.execute("SELECT userID FROM Users WHERE email = %(email)s", {"email": email})
            user = mycursor.fetchone()
            userID = user[0]
            mycursor.reset()
            mycursor.execute("SELECT tokenID FROM Tokens WHERE userID = %(userID)s", {"userID": userID})
            tokenCheck = mycursor.fetchone()
            if tokenCheck is not None:
                mycursor.reset()
                mycursor.execute("UPDATE Tokens SET token = %(token)s WHERE userID = %(userID)s", ({"token": token, "userID": userID}))
                db.commit()
                return jsonify({"token": token})
            else:
                mycursor.execute("INSERT INTO Tokens (userID, token) VALUES (%(userID)s,%(token)s)",{"userID": userID, "token": token})
                db.commit()
                return jsonify({"token": token})
        else:
            return jsonify({"message": "Incorrect Password"})