from flask import jsonify, Flask
from carRegistationApi import carRegistrationBP
from historyApi import historyBP
from showCarsApi import showCarsBP
from showUserApi import showUserBP
from tripRegistrationApi import tripRegistrationBP
from userLoginApi import userLoginBP
from userRegistrationApi import userRegistrationBP
from locationApi import addressToLocationBP
from stripeMethodApi import stripeMethodBP
from paypalMethodApi import paypalMethodBP

app = Flask(__name__)
app.register_blueprint(showCarsBP)
app.register_blueprint(userRegistrationBP)
app.register_blueprint(historyBP)
app.register_blueprint(tripRegistrationBP)
app.register_blueprint(carRegistrationBP)
app.register_blueprint(showUserBP)
app.register_blueprint(userLoginBP)
app.register_blueprint(addressToLocationBP)
app.register_blueprint(stripeMethodBP)
app.register_blueprint(paypalMethodBP)


@app.route('/')
def index():
    return jsonify({"message": "Index"})