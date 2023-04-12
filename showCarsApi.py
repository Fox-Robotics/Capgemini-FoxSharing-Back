from validations import *
from databaseConection import *

from flask import Blueprint
blueprintShowCarsApi = Blueprint('showCarsBlueprint', __name__)

@blueprintShowCarsApi .route('/cars', methods=['GET'])
def cars():
    mycursor.execute("SELECT * FROM Cars")
    row = [x[0] for x in mycursor.description]
    data = mycursor.fetchall()
    carsData = []
    for result in data:
        carsData.append(dict(zip(row, result)))

    return jsonify({"Cars": carsData})
