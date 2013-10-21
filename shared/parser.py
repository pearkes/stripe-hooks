import stripe
from .app import app
from shared.mail import send_notification, send_receipt
from shared.helpers import CleanParseException, format_stripe_object


def parse_hook(payload):
    """Parses a dictionary representation of the stripe webhook
    by requesting a new version of the event by it's ID from the stripe
    API. This is done for security reasons.

    See https://github.com/pearkes/stripe-hooks#security
    """
    # Request the event from Stripe, raises stripe.InvalidRequestError if
    # not found
    event = stripe.Event.retrieve(payload.get("id"))

    # Determine what type of event it is and send any nots/receipts
    determine_event_type(event)


def determine_event_type(event):
    "Determines what type of hook an event is"

    config = app.config['email']

    if config['notifications'].get(event.type):
        parse_notification(event)

    if config['receipts'].get(event.type):
        parse_receipt(event)


def parse_notification(event):
    "Parse the details of an event for a notification"
    # Format the data for the email
    data = format_stripe_object(event.data.object)

    send_notification(event.type, data)


def parse_receipt(event):
    "Parse the details of an event for a receipt"
    recepient = find_email_address(event.data.object)

    # A CleanParseException tells the webhook to respond
    # succesfully with a message back to the stripe dashboard
    if not recepient:
        raise CleanParseException(
            "Can't find customer email address for receipt")

    # Format the data for the email
    data = format_stripe_object(event.data.object)

    send_receipt(event.type, recepient, data)


def find_email_address(stripe_object):
    """Looks for an email in a stripe object, returns an email or None
    if there wasn't one found, which may be the case sometimes."""

    # Some objects have an "email" field, this makes it easy
    email = stripe_object.get("email")

    if email:
        return email

    # Others have a customer ID, we'll need to request
    # it from Stripe in this case.
    customer = stripe_object.get("customer")

    if customer:
        full_customer = stripe.Customer.retrieve(customer)
        if full_customer.email:
            return full_customer.email
