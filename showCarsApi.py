from flask import Flask, jsonify, request
from validations import *
from databaseConection import *

app = Flask(__name__)

@app.route('/cars', methods=['GET'])
def cars():
    mycursor.execute("SELECT * FROM Cars")
    row = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    carsData = []
    for result in data:
        carsData.append(dict(zip(row, result)))

    return jsonify({"Cars": carsData})

if __name__ == '__main__':
    app.run(debug=True, port=1000)