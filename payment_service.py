import stripe

def process_payment(amount, currency="usd", payment_method=None):
    # Migration: Use PaymentIntent (stripe==5.4.0, API v2022-11-15)
    # Stripe expects amount in the smallest currency unit (e.g., cents for USD)
    # If amount is in dollars, convert to cents
    if currency.lower() == "usd" and amount < 50:
        # Heuristic: likely passed in dollars, convert to cents
        amount = int(amount * 100)

    if payment_method:
        # Immediate server-side confirm (legacy token or payment_method id)
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method=payment_method,
            payment_method_types=["card"],
            confirm=True,
            description="Order Payment"
        )
        # latest_charge replaces charges (removed in v2022-11-15)
        return intent.latest_charge
    else:
        # Client-side completion flow
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=["card"],
            description="Order Payment"
        )
        return intent