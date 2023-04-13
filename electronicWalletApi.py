from flask import Blueprint, jsonify, request, redirect, url_for
from validations import tokenRequired
from databaseConection import mycursor, db

electronicWalletBP = Blueprint('electronicWalletBP', __name__)

@electronicWalletBP.route('/wallet/stripe', methods=['POST'])
@tokenRequired
def walletStripe():
    token = request.json['token']
    mycursor.execute("SELECT userID from Tokens WHERE token = %(token)s", {"token": token})
    user = mycursor.fetchone()
    userID = user[0]

    quantity = request.json['total']

    payment_url = url_for('stripeMethodBP.walletStripePayment', method='GET', _external=True, total=quantity, userID=userID)

    return redirect(payment_url)

@electronicWalletBP.route('/wallet/paypal', methods=['POST'])
@tokenRequired
def walletPaypal():
    token = request.json['token']
    mycursor.execute("SELECT userID from Tokens WHERE token = %(token)s", {"token": token})
    user = mycursor.fetchone()
    userID = user[0]

    quantity = request.json['total']

    payment_url = url_for('paypalMethodBP.walletPaypalPayment', _external=True, total=quantity, userID=userID)

    return redirect(payment_url)

@electronicWalletBP.route('/wallet/successful', methods=['GET'])
def walletSuccessful():
    quantity = request.args.get('total')
    userID = request.args.get('userID')

    mycursor.execute("INSERT INTO Wallet (quantity, userID) VALUES (%(quantity)s,%(userID)s)", {"quantity":quantity, "userID":userID})
    db.commit()

    return jsonify({"message": "Successfully Wallet Deposit"})

@electronicWalletBP.route('/wallet/cancel', methods=['GET'])
def walletCancel():
    return jsonify({"message": "Wallet Deposit Canceled"})

@electronicWalletBP.route('/trip/cancel', methods=['GET'])
def tripCancel():
    return jsonify({"message": "Trip Canceled"})

@electronicWalletBP.route('/trip/successfully', methods=['GET'])
def tripSuccessful():
    tripID = request.args.get('tripID')
    quantity = request.args.get('total')

    mycursor.execute("UPDATE Trips SET total=%(total)s WHERE tripID=%(tripID)s", {"total": quantity, "tripID": tripID})
    db.commit()

    return jsonify({"message": "Trip Paid Successfully"})
