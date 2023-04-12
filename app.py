from flask import Blueprint, jsonify, Flask
from showCarsApi import showCarsBP
from userRegistrationApi import userRegistrationBP
from historyApi import historyBP
from tripRegistrationApi import tripRegistrationBP
from carRegistationApi import carRegistrationBP
from showUserApi import showUserBP
from userLoginApi import userLoginBP

app = Flask(__name__)
app.register_blueprint(showCarsBP)
app.register_blueprint(userRegistrationBP)
app.register_blueprint(historyBP)
app.register_blueprint(tripRegistrationBP)
app.register_blueprint(carRegistrationBP)
app.register_blueprint(showUserBP)
app.register_blueprint(userLoginBP)

@app.route('/')
def index():
    return jsonify({"message": "Index"})

if __name__ == '__main__':
    app.run(debug=True, port=1000)
