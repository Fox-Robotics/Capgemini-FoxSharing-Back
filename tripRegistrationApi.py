from flask import Flask, jsonify, request
from validations import *
from databaseConection import *

app = Flask(__name__)

@app.route('/trip', methods=['POST'])
def trip():
    initialLocation = request.json['initialLocation']
    finalLocation = request.json['finalLocation']
    time = request.json['time']
    kmTraveled = request.json['kmTraveled']
    publicKey = request.json['publicKey']

    if valKilometros(kmTraveled):
        newTrip = {
            ""
        }

if __name__ == '__main__':
    app.run(debug=True, port=1000)