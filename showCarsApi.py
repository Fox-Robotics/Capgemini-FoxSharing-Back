from flask import jsonify, Blueprint
from databaseConection import mycursor

showCarsBP = Blueprint('blueprint', __name__)

@showCarsBP.route('/cars', methods=['GET'])
def cars():
    mycursor.execute("SELECT * FROM Cars")
    row = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    carsData = []
    for result in data:
        carsData.append(dict(zip(row, result)))

    return jsonify({"Cars": carsData})