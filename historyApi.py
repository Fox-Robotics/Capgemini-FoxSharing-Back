from flask import Flask, jsonify, request, Blueprint
from validations import tokenRequired
from databaseConection import mycursor

historyBP = Blueprint('historyBP', __name__)

@historyBP.route('/history', methods=['POST'])
@tokenRequired
def history():
    token = request.json['token']
    mycursor.execute("SELECT userID from Tokens WHERE token = %(token)s", {"token": token})
    user = mycursor.fetchone()
    userID = user[0]

    mycursor.execute("SELECT * FROM Trips WHERE userID = %(userID)s", {"userID": userID})
    row = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    tripsData = []
    for result in data:
        tripsData.append(dict(zip(row, result)))

    return jsonify({"Trips": tripsData})
