from flask import Flask, jsonify, request, Blueprint, redirect, url_for
from validations import valKilometers
from databaseConection import mycursor, db
import datetime

tripRegistrationBP = Blueprint('tripRegistrationBP', __name__)
@tripRegistrationBP.route('/trip', methods=['POST'])
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

    if valKilometers(kmTraveled):
        newTrip = {
            "userID": userID,
            "initialLocation": initialLocation,
            "finalLocation": finalLocation,
            "time": time,
            "kmTraveled": kmTraveled,
            "publicKey": publicKey,
            "total": "000"
        }
        print(newTrip)
        mycursor.execute("INSERT INTO Trips (userID,initialLocation,finalLocation,time,kmTraveled,publicKey,total) VALUES (%(userID)s,%(initialLocation)s,%(finalLocation)s,%(time)s,%(kmTraveled)s,%(publicKey)s,%(total)s)", newTrip)
        db.commit()
        mycursor.reset()
        mycursor.execute("SELECT tripID FROM Trips WHERE publicKey=%(publicKey)s", {"publicKey": publicKey})
        trip = mycursor.fetchone()
        tripID = trip[0]
        payment_url = url_for('paypalMethodBP.tripPaypalPayment', _external=True, tripID=tripID, kmTraveled=kmTraveled)
        return redirect(payment_url)
    else:
        return jsonify({"message": "Trip Registered Unsuccessfully"})