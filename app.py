from flask import Flask
from carRegistationApi import blueprintCarRegistrationApi
from showCarsApi import blueprintShowCarsApi
from showUserApi import blueprintShowUserApi
from tripRegistrationApi import blueprintTripRegistration
from userLoginApi import blueprintUserLogin
from userRegistrationApi import blueprintUserRegistration

app = Flask(__name__)
app.register_blueprint(blueprintCarRegistrationApi)
app.register_blueprint(blueprintShowCarsApi)
app.register_blueprint(blueprintShowUserApi)
app.register_blueprint(blueprintTripRegistration)
app.register_blueprint(blueprintUserLogin)
app.register_blueprint(blueprintUserRegistration)

if __name__ == '__main__':
   app.run(debug=True, port=5000)