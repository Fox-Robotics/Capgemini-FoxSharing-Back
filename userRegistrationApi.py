from flask import Flask, jsonify, request
import bcrypt
import mysql.connector
from validations import *
from databaseConection import *

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def registerUser():
    name = request.json['name']
    firstLastName = request.json['firstLastName']
    secondLastName = request.json['secondLastName']
    password = request.json['password']
    email = request.json['email']

    if valNames(name) and valNames(firstLastName) and (valNames(secondLastName) or secondLastName is None) and valPassword(password) and valEmail(email):
        hash = bcrypt.hashpw(password.encode('UTF-8'), bcrypt.gensalt(4))

        newUser = {
            "name": name,
            "firstLastName": firstLastName,
            "secondLastName": secondLastName,
            "hash": hash,
            "email": email
        }

        mycursor.execute("INSERT INTO Users (name, firstLastName, secondLastName, hash, email) VALUES (%(name)s, %(firstLastName)s, %(secondLastName)s, %(hash)s, %(email)s)", newUser)
        db.commit()
        return jsonify({"message": "User Signed Up Successfully"})
    else:
        return jsonify({"message": "User Signed Up Unsuccessfully"})

if __name__ == '__main__':
    app.run(debug=True, port=1000)