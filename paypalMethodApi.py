import paypalrestsdk
from config import paypalClientID, paypalClientSecret
from flask import Blueprint, redirect
from urllib import request

paypalMethodBP = Blueprint('paypalMethodBP', __name__)


@paypalMethodBP.route('/payment/paypal')
def paypalPayment():
    paypalrestsdk.configure({
        "mode": "sandbox",
        "client_id": paypalClientID,
        "client_secret": paypalClientSecret
    })

    total = 1000

    product = 'normalTrip'
    price = total

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:5000/execute_payment",
            "cancel_url": "http://localhost:5000/cancel_payment"
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
                "total": price,
                "currency": "MXN"
            },
            "description": "Item Description"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = str(link.href)
                return redirect(redirect_url)
    else:
        print(payment.error)

@paypalMethodBP.route('/execute_payment')
def execute_payment():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return "Payment completed successfully."
    else:
        return str(payment.error)

@paypalMethodBP.route('/cancel_payment')
def cancel_payment():
    return print("Payment canceled.")