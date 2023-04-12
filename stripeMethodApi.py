import stripe
from flask import Flask, jsonify, request
import mysql.connector
from validations import *
from databaseConection import *
import stripe

app = Flask(__name__)

@app.route('/payment')
def payment():
    stripe.api_key = stripeSecretKey

    stripe.checkout.Session.create(
        cancel_url="https://facebook.com",
        line_items=[{"price": 'price_1Mvn5eCP2A27V5KAAOiGYIaZ', "quantity": 67}],
        mode="payment",
        success_url="https://youtube.com",
    )

    return jsonify({'message':"hi"})

if __name__ == '__main__':
    app.run(debug=True, port=1000)