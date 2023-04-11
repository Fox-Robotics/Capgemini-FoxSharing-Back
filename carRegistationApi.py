from flask import Flask, jsonify, request
from validations import *
from databaseConection import *

app = Flask(__name__)

@app.route('/registerCar', methods=['POST'])
def registerCar():
    brand = request.json['brand']
    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    plate = request.json['plate']
    serialNum = request.json['serialNum']
    kmLiter = request.json['kmLiter']
    mileage = request.json['mileage']
    status = request.json['status']
    latitude = request.json['latitude']
    longitude = request.json['longitude']

    print(brand,model,year,color,plate,serialNum,kmLiter,mileage,status,latitude,longitude)

    if valNames(brand) and valModelo(model) and valNames(color) and valPlacas(plate) and valKilometros(kmLiter) and valKilometros(mileage):
        newCar = {
            "brand": brand,
            "model": model,
            "year": year,
            "color": color,
            "plate": plate,
            "serialNum": serialNum,
            "kmLiter": kmLiter,
            "mileage": mileage,
            "status": status,
            "latitude": latitude,
            "longitude": longitude
        }

        mycursor.execute("INSERT INTO Cars (brand,model,color,plate,serialNum,kmLiter,mileage,status,latitude,longitude,year) VALUES (%(brand)s,%(model)s,%(color)s,%(plate)s,%(serialNum)s,%(kmLiter)s,%(mileage)s,%(status)s,%(latitude)s,%(longitude)s,%(year)s)", newCar)
        db.commit()

        return jsonify({"message": "Car Registered Successfully"})
    else:
        return jsonify({"message": "Car Registered Unsuccessfully"})

if __name__ == '__main__':
    app.run(debug=True, port=1000)