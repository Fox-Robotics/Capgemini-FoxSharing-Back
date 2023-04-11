from flask import Flask, jsonify, request
from validations import *
from databaseConection import *

app = Flask(__name__)

@app.route('/user', methods=['POST'])
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


if __name__ == '__main__':
    app.run(debug=True, port=1000)