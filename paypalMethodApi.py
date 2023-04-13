import paypalrestsdk
from config import paypalClientID, paypalClientSecret
from flask import Blueprint, redirect, request, url_for, jsonify

paypalMethodBP = Blueprint('paypalMethodBP', __name__)

@paypalMethodBP.route('/trip/payment/paypal', methods=['GET'])
def tripPaypalPayment():
    paypalrestsdk.configure({
        "mode": "sandbox",
        "client_id": paypalClientID,
        "client_secret": paypalClientSecret
    })

    kmTraveled = request.args.get('kmTraveled')
    tripID = request.args.get('tripID')

    print(kmTraveled, tripID)

    total = kmTraveled * 100 * 20

    product = 'normalTrip'

    success_url = url_for('electronicWalletBP.tripSuccessful', method='GET', _external=True, total=total, tripID=tripID)
    cancel_url = url_for('electronicWalletBP.tripCancel', _external=True)

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": success_url,
            "cancel_url": cancel_url
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": product,
                    "sku": "Item SKU",
                    "price": total,
                    "currency": "MXN",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": total,
                "currency": "MXN"
            },
            "description": "Item Description"
        }]
    })

    print("here")

    if payment.create():
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                print(redirect_url)
                return redirect(redirect_url)
    else:
        print(payment.error)
        return jsonify({"message": "An error has occurred"})

@paypalMethodBP.route('/wallet/payment/paypal', methods=['GET'])
def walletPaypalPayment():
    paypalrestsdk.configure({
        "mode": "sandbox",
        "client_id": paypalClientID,
        "client_secret": paypalClientSecret
    })

    userID = request.args.get('userID')
    total = request.args.get('total')

    product = 'walletDeposit'

    success_url = url_for('electronicWalletBP.walletSuccessful', method='GET', _external=True, total=total, userID=userID)
    cancel_url = url_for('electronicWalletBP.walletCancel', _external=True)

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": success_url,
            "cancel_url": cancel_url
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": product,
                    "sku": "Item SKU",
                    "price": total,
                    "currency": "MXN",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": total,
                "currency": "MXN"
            },
            "description": "Item Description"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                print(redirect_url)
                return redirect(redirect_url)
    else:
        print(payment.error)
