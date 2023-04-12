from flask import Blueprint, redirect
from config import stripeSecretKey
import stripe

paymentMethodBP = Blueprint('paymentMethodBP', __name__)

@paymentMethodBP.route('/payment')
def payment():
    stripe.api_key = stripeSecretKey

    total = 1000

    product = 'normalTrip'
    price = total

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
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )

    checkout_url = session.url

    return redirect(checkout_url)