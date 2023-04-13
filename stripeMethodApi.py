from flask import Blueprint, redirect, request, json, jsonify, url_for
from config import stripeSecretKey
from validations import tokenRequired
import stripe
from databaseConection import mycursor

stripeMethodBP = Blueprint('stripeMethodBP', __name__)

@stripeMethodBP.route('/trip/payment/stripe', methods=['GET'])
@tokenRequired
def tripStripePayment():
    stripe.api_key = stripeSecretKey

    token = request.json['token']
    mycursor.execute("SELECT userID from Tokens WHERE token = %(token)s", {"token": token})
    user = mycursor.fetchone()
    userID = user[0]

    kmTraveled = request.args.get('kmTraveled')
    total = request.args.get('total')

    total = kmTraveled * 100 * 20

    product = 'normalTrip'
    price = total

    success_url = url_for('electronicWalletBP.triptSuccessful', method='GET', _external=True, total=total, userID=userID)
    cancel_url = url_for('electronicWalletBP.tripCancel', _external=True)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'mxn',
                'product_data': {
                    'name': product,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )

    checkout_url = session.url
    print(checkout_url)
    return jsonify({"message": "hello there"})

@stripeMethodBP.route('/wallet/payment/stripe', methods=['GET'])
def walletStripePayment():
    stripe.api_key = stripeSecretKey

    userID = request.args.get('userID')
    total = request.args.get('total')

    product = 'walletDeposit'
    price = total

    success_url = url_for('electronicWalletBP.walletSuccessful', method='GET', _external=True, total=total, userID=userID)
    cancel_url = url_for('electronicWalletBP.walletCancel', _external=True)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'mxn',
                'product_data': {
                    'name': product,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=success_url,
        cancel_url=cancel_url,
    )

    checkout_url = session.url
    print(checkout_url)
    return jsonify({"message": "hello there"})