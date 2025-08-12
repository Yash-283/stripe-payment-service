# payment_service.py (before)
import stripe

def process_payment(amount, currency="usd", source=None):
    # Deprecated method in Stripe v2022-11-15
    return stripe.Charge.create(
        amount=amount,
        currency=currency,
        source=source,
        description="Order Payment"
    )
