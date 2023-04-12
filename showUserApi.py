from validations import *
from databaseConection import *
from flask import Blueprint
blueprintShowUserApi = Blueprint('showUserBlueprint', __name__)


@blueprintShowUserApi.route('/user', methods=['POST'])
@tokenRequired
def user():
    token = request.json['token']

    mycursor.execute("SELECT userID FROM Tokens WHERE token = %(token)s", {"token": token})
    user = mycursor.fetchone()
    userID = user[0]

    mycursor.execute("SELECT name,firstLastName,secondLastName,email FROM Users WHERE userID = %(userID)s", {"userID": userID})
    row = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    userData = []
    for result in data:
        userData.append(dict(zip(row,result)))
    return jsonify({"User": userData})

