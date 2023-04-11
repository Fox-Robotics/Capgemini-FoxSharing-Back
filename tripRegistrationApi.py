from flask import Flask, jsonify, request
from validations import *
from databaseConection import *
import datetime

app = Flask(__name__)

@app.route('/trip', methods=['POST'])
def trip():
    token = request.json['token']
    initialLocation = request.json['initialLocation']
    finalLocation = request.json['finalLocation']
    time = datetime.datetime.utcnow()
    kmTraveled = request.json['kmTraveled']
    publicKey = request.json['publicKey']

    mycursor.execute("SELECT userID FROM Tokens WHERE token = %(token)s", {"token": token})
    values = mycursor.fetchone()
    userID = values[0]

    if valKilometros(kmTraveled):
        newTrip = {
            "userID": userID,
            "initialLocation": initialLocation,
            "finalLocation": finalLocation,
            "time": time,
            "kmTraveled": kmTraveled,
            "publicKey": publicKey
        }

        mycursor.execute("INSERT INTO Trips (userID,initialLocation,finalLocation,time,kmTraveled,publicKey) VALUES (%(userID)s,%(initialLocation)s,%(finalLocation)s,%(time)s,%(kmTraveled)s,%(publicKey)s)", newTrip)
        db.commit()
        return jsonify({"message": "Trip Registered Successfully"})
    else:
        return jsonify({"message": "Trip Registered Unsuccessfully"})

if __name__ == '__main__':
    app.run(debug=True, port=1000)